#!/usr/bin/bash

echo "navigating to project directory"

cd ~/gitgators-lauren-wasay/

echo "Navigated to project directory."
echo "---------------------------------------------"

echo "running git fetch"

git fetch && git reset origin/main --hard

echo "Ran git fetch."
echo "---------------------------------------------"

echo "running docker compose down"

docker compose -f ~/gitgators-lauren-wasay/docker-compose.prod.yml down

echo "ran docker compose down"
echo "---------------------------------------------"

echo "running docker compose up"

docker compose -f ~/gitgators-lauren-wasay/docker-compose.prod.yml up -d --build

echo "ran docker compose up"
echo "---------------------------------------------"
