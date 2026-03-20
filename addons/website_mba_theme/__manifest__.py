{
    'name': 'MBA Consultings Website Theme',
    'version': '1.1',
    'category': 'Theme/Corporate',
    'summary': 'Diseño premium monocromático para MBA Consultings',
    'description': 'Módulo basado en Odoo 19 Community sobre OCI y localización Panamá.',
    'depends': ['website', 'website_crm'],
    'data': [
        'views/service_pages.xml',
        'views/pages.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_mba_theme/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
