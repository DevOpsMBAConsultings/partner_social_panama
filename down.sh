#!/bin/bash
# down-local.sh - Stop Docker and Colima

echo ">>> Stopping Docker Compose..."
docker compose down

echo ">>> Stopping Colima..."
colima stop
