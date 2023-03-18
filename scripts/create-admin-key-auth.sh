#/bin/bash

# Generate a key for Kong Admin API

echo "Generating a key for Kong Admin API ..."
echo "This key will be used by Konga to connect to Kong Admin API"
echo "---------------------------------"

# Creating admin-api service
curl -s -X POST 'http://localhost:8001/services/' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "name": "admin-api",
    "host": "localhost",
    "port": 8001
}'

# Creating admin-api route
curl -s -X POST 'http://localhost:8001/services/admin-api/routes' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "paths": ["/admin-api"]
}'

# Creating admin-api key-auth plugin
curl -s -X POST 'http://localhost:8001/services/admin-api/plugins' \
  -data "name=key-auth"

# Creating consumer
curl -s -X POST 'http://localhost:8001/consumers/' \
  --form 'username=konga' \
  --form 'custom_id=cebd360d-3de6-4f8f-81b2-31575fe9846a'

# Creating key for consumer
token=$(curl -s -X POST 'http://localhost:8001/consumers/konga/key-auth' | sed -n 's/.*"key":"\([^"]*\)".*/\1/p')

echo 'Select "Key Auth" as Authentication Type Introduce the following data in the "Update connection section" of Konga:\n'
echo 'Name: admin-api'
echo 'Loopback API URL: http://kong:8000/admin-api'
echo 'API KEY: '$token
