#!/bin/bash
set -x
NODE_IP=$(kubectl get nodes -o jsonpath='{ $.items[0].status.
addresses[?
(@.type=="ExternalIP")].address }')
NODE_PORT=$(kubectl get svc calculator-service -o=jsonpath='{.
spec.ports[0].nodePort}')
./gradlew acceptanceTest -Dcalculator.url=http://${NODE_
IP}:${NODE_PORT}