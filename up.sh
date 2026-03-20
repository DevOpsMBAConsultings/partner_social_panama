#!/bin/bash
# setup-local.sh - Start Colima, Docker, and Provision Odoo

# Default DB name, can be overridden by first command line argument
DB_NAME=${1:-postgres}

echo ">>> Starting Colima..."
colima start

echo ">>> Starting Docker Compose..."
docker compose up -d

echo ">>> Waiting for Odoo to be ready (10s)..."
sleep 10

# Check if database is initialized, if not, initialize it
if docker compose exec odoo odoo -c /etc/odoo/odoo.conf -d "$DB_NAME" --stop-after-init 2>&1 | grep -q "Database $DB_NAME not initialized"; then
    echo ">>> Initializing database '$DB_NAME'..."
    docker compose exec odoo odoo -c /etc/odoo/odoo.conf -d "$DB_NAME" -i base --stop-after-init
fi

echo ">>> Running Panama Provisioning Standard on database '$DB_NAME'..."
./provision.sh "$DB_NAME"

echo ">>> Startup Complete. Odoo is at http://localhost:8069"
docker compose ps
