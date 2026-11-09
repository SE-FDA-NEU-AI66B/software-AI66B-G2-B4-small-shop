#!/bin/sh
set -eu

: "${TS_AUTHKEY:?Missing TS_AUTHKEY environment variable}"

mkdir -p /var/lib/tailscale /var/run/tailscale

echo "===== START TAILSCALE DAEMON ====="

tailscaled \
  --state=/var/lib/tailscale/tailscaled.state \
  --socket=/var/run/tailscale/tailscaled.sock \
  --tun=userspace-networking &

TAILSCALE_PID=$!

# Wait for the Unix socket, not for a successful login.
READY=0

for i in $(seq 1 30); do
    if [ -S /var/run/tailscale/tailscaled.sock ]; then
        READY=1
        break
    fi

    if ! kill -0 "$TAILSCALE_PID" 2>/dev/null; then
        echo "ERROR: tailscaled process exited"
        exit 1
    fi

    sleep 1
done

if [ "$READY" -ne 1 ]; then
    echo "ERROR: Tailscale socket was not created"
    exit 1
fi

echo "===== CONNECT TO TAILSCALE ====="

tailscale \
  --socket=/var/run/tailscale/tailscaled.sock \
  up \
  --authkey="${TS_AUTHKEY}" \
  --hostname=render-yums-test \
  --accept-dns=false

echo "===== TAILSCALE STATUS ====="

tailscale \
  --socket=/var/run/tailscale/tailscaled.sock \
  status

echo "===== TEST WINDOWS DEVICE ====="

tailscale \
  --socket=/var/run/tailscale/tailscaled.sock \
  ping \
  --timeout=10s \
  100.115.168.64 || echo "WARNING: Windows ping test failed"

echo "===== START FASTAPI ====="

exec uvicorn main:app --host 0.0.0.0 --port "${PORT:-10000}"