#!/bin/bash
# Run Odoo Provisioning inside the container
docker compose exec odoo python3 /opt/odoo/provisioning/provision_all.py "$@"
