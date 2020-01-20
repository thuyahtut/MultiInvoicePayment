# -*- coding: utf-8 -*-
{
    'name': "Multiple Invoice Payment",

    'summary': "Easy to register multiple invoice payments.",

    'description': "Easy to register multiple invoice payments.",

    'author': "TrioAnderson",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends' : ['base_setup', 'product', 'analytic', 'web_planner', 'portal'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': 1,
    'application': True,
}