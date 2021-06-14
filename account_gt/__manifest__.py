# -*- coding: utf-8 -*-
{
    'name': "account_gt",

    'summary': """ Conta extra para guate """,

    'description': """
        Conta extra para guate
    """,

    'author': "JS",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['account','base'],

    'data': [
        'views/res_partner_views.xml',
        'views/account_gt_views.xml',
        'views/account_move_views.xml',
        'views/account_payment_view.xml',
        'data/ir_sequence_data.xml',
    ],
}
