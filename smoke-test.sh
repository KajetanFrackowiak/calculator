#!/bin/bash
set -e  # Exit immediately if a command exits with non-zero status

# Get the external IP and port of the deployed service
NODE_IP=$(kubectl get nodes -o jsonpath='{ $.items[0].status.addresses[?(@.type=="ExternalIP")].address }')
NODE_PORT=$(kubectl get svc calculator-service -o=jsonpath='{.spec.ports[0].nodePort}')

echo "Testing calculator service at http://${NODE_IP}:${NODE_PORT}"

# Simple smoke test - just check if the add endpoint is responding correctly
RESPONSE=$(curl -s "http://${NODE_IP}:${NODE_PORT}/add?a=1&b=2")
EXPECTED='"result":3'

if [[ $RESPONSE == *"$EXPECTED"* ]]; then
    echo "✅ Smoke test passed!"
    exit 0
else
    echo "❌ Smoke test failed! Expected '$EXPECTED' in response but got: $RESPONSE"
    exit 1
fi