#!/bin/bash
# ls-db.sh - List all existing databases in the Docker container

if ! docker info > /dev/null 2>&1; then
    echo "ERROR: Docker is not running. Please run ./up.sh first."
    exit 1
fi

echo ">>> Existing Odoo Databases:"
docker compose exec db psql -U odoo -t -c "SELECT datname FROM pg_database WHERE datistemplate = false AND datname NOT IN ('postgres', 'template1');"
