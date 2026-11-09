import select
import socket
import socketserver
import socks


MYSQL_TAILSCALE_IP = "100.115.168.64"
MYSQL_PORT = 3306

SOCKS_HOST = "127.0.0.1"
SOCKS_PORT = 1055

RELAY_HOST = "127.0.0.1"
RELAY_PORT = 13306


def handle_connection(client):
    remote = None

    try:
        remote = socks.socksocket()
        remote.set_proxy(
            socks.SOCKS5,
            SOCKS_HOST,
            SOCKS_PORT
        )
        remote.connect((MYSQL_TAILSCALE_IP, MYSQL_PORT))

        sockets = [client, remote]

        while True:
            readable, _, exceptional = select.select(
                sockets, [], sockets
            )

            if exceptional:
                break

            for source in readable:
                data = source.recv(65536)

                if not data:
                    return

                destination = remote if source is client else client
                destination.sendall(data)

    except Exception as error:
        print(f"MySQL relay connection error: {error}")

    finally:
        client.close()

        if remote:
            remote.close()


class RelayServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


class RelayHandler(socketserver.BaseRequestHandler):
    def handle(self):
        handle_connection(self.request)


if __name__ == "__main__":
    print(
        f"MySQL TCP relay listening on "
        f"{RELAY_HOST}:{RELAY_PORT}"
    )

    with RelayServer(
        (RELAY_HOST, RELAY_PORT),
        RelayHandler
    ) as server:
        server.serve_forever()