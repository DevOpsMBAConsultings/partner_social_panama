{
    'name': 'ST Car Rental Management',
    'version': '1.0.0',
    'category': 'Operations/Fleet',
    'summary': 'Comprehensive Car Rental Management System inspired by RentlySoft',
    'description': """
Car Rental Management System
============================
Key Features:
- Fleet management integration (Fleet)
- Dynamic rental rates (Daily, Weekly, Monthly)
- Rental booking workflow based on Sale Orders
- Digital "In & Out" inspections with photo support
- Traffic fine management and tracking
    """,
    'author': 'Antigravity / Siteck',
    'website': 'https://www.siteck.com',
    'depends': [
        'base',
        'fleet',
        'sale_management',
        'mail',
        'website',
        'loyalty',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/rental_rate_views.xml',
        'views/rental_location_views.xml',
        'views/fleet_vehicle_views.xml',
        'views/rental_order_views.xml',
        'views/rental_inspection_views.xml',
        'views/rental_fine_views.xml',
        'views/rental_dashboard_views.xml',
        'views/rental_menus.xml',
        'views/website_rental_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # Reserved for custom JS/CSS
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
