{
    'name': "Burhansir Task",
    'version': '16.0.1.0.0',
    'author': 'Ramiz Belim',
    'sequence': 10,
    'description': """ Task on Context by Burhansir """,
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',

        'wizard/wizard_views.xml',

        'views/sale_order_views.xml',
        'views/purchase_views.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
