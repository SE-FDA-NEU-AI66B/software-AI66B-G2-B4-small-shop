#!/bin/sh
set -eu

: "${TS_AUTHKEY:?Missing TS_AUTHKEY environment variable}"

mkdir -p /var/lib/tailscale /var/run/tailscale

# Start Tailscale in userspace networking mode.
tailscaled \
  --state=/var/lib/tailscale/tailscaled.state \
  --socket=/var/run/tailscale/tailscaled.sock \
  --tun=userspace-networking \
  --socks5-server=127.0.0.1:1055 &

# Wait for Tailscale daemon.
READY=0
for i in $(seq 1 30); do
    if tailscale --socket=/var/run/tailscale/tailscaled.sock status >/dev/null 2>&1; then
        READY=1
        break
    fi
    sleep 1
done

if [ "$READY" -ne 1 ]; then
    echo "Tailscale daemon did not start"
    exit 1
fi

# Join the private Tailscale network.
tailscale --socket=/var/run/tailscale/tailscaled.sock up \
  --authkey="${TS_AUTHKEY}" \
  --hostname=render-yums-test \
  --accept-dns=false

echo "===== TAILSCALE STATUS ====="
tailscale --socket=/var/run/tailscale/tailscaled.sock status

echo "===== TEST WINDOWS DEVICE ====="
tailscale --socket=/var/run/tailscale/tailscaled.sock ping \
  --timeout=5s 100.115.168.64 || echo "Windows ping test failed"

echo "===== START FASTAPI ====="
exec uvicorn main:app --host 0.0.0.0 --port "${PORT:-10000}"