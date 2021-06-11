# -*- coding: utf-8 -*-


{
    'name': 'FEL DIGIFACT',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Módulo para facturacion en linea DIGIFACT',
    'description': """

""",
    'depends': ['account'],
    'data': [
        'views/account_view.xml',
        'views/res_company_views.xml',
        'views/account_invoice_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
