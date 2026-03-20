# -*- coding: utf-8 -*-
{
    "name": "MBA Panama Accounting Dashboard",
    "summary": """
        Provides a pre-configured BI Dashboard with accounting reports and KPIs 
        relevant for Panamanian companies.
    """,
    "description": """
        This module extends the Synconics BI Dashboard to create a specialized 
        accounting dashboard for Panama. It includes visualizations for:
        - ITBMS Summary (Collected vs. Paid)
        - Withholding Tax (Retenciones)
        - "Informe de Compras" Data Summary
        - Sales by Province Map
    """,
    "author": "MBA Consultings (via Gemini)",
    "website": "https://www.mbaconsultings.com",
    "category": "Accounting/Localization",
    "version": "19.0.1.0.0",
    "license": "LGPL-3",
    "depends": [
        "account",
        "synconics_bi_dashboard",
        "l10n_pa",  # Assuming standard Panama localization is installed
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/dashboard_data.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
