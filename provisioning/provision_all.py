#!/usr/bin/env python3
import os
import subprocess
import sys

# Configuration
ODOO_CONF = "/etc/odoo/odoo.conf"
# Default DB name, can be overridden by first command line argument
DB_NAME = sys.argv[1] if len(sys.argv) > 1 else "postgres"
ODOO_HOME = "/usr/lib/python3/dist-packages" # Standard path in Odoo Docker
COUNTRY_CODE = "PA"
LANG_CODE = "es_PA"

SCRIPTS_DIR = "/opt/odoo/provisioning/scripts"

PROVISIONING_ORDER = [
    "set_default_country.py",
    "set_panama_states.py",
    "set_default_paperformat.py",
    "set_contacts_default_view_kanban.py",
    "set_partner_tags.py",
    "set_default_taxes_pa.py",
    "set_itbms_taxes_pa.py",
    "set_tax_retencion_impuestos.py",
    "set_fiscal_position_exento.py",
    "set_fiscal_position_retencion.py",
    "set_payment_terms_pa.py",
    "set_default_sales_journal.py",
    "set_default_credit_notes_journal.py",
    "set_default_products_pa.py",
    "set_sale_uom_packaging.py",
]

def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if not os.path.exists(script_path):
        print(f"ERROR: Script {script_name} not found at {script_path}")
        return False

    print(f"\n>>> Running {script_name}...")
    
    env = os.environ.copy()
    env["ODOO_CONF"] = ODOO_CONF
    env["DB_NAME"] = DB_NAME
    env["ODOO_COUNTRY_CODE"] = COUNTRY_CODE
    env["ODOO_LANG"] = LANG_CODE

    try:
        # Run with current python3
        result = subprocess.run(
            [sys.executable, script_path],
            env=env,
            capture_output=False,
            text=True
        )
        if result.returncode != 0:
            print(f"FAILED: {script_name} exited with code {result.returncode}")
            return False
        return True
    except Exception as e:
        print(f"EXCEPTION: {script_name} failed with {e}")
        return False

def main():
    print("Starting Odoo Provisioning for Panama...")
    print(f"DB: {DB_NAME}, Conf: {ODOO_CONF}")
    
    success_count = 0
    for script in PROVISIONING_ORDER:
        if run_script(script):
            success_count += 1
        else:
            print(f"\nCRITICAL: Provisioning failed at {script}. Stopping.")
            sys.exit(1)
            
    print(f"\nPROVISIONING COMPLETE: {success_count}/{len(PROVISIONING_ORDER)} scripts succeeded.")

if __name__ == "__main__":
    main()
