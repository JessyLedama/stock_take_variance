# -*- coding: utf-8 -*-
{
    'name': "Stock Take Variance",

    'summary': """
        Extension of Inventory Valuation. """,

    'description': """
        Extension of Inventory Valuation to include:
        
        1) 'Variance' after 'Real Quantity'.
        2) Stock Variance Report.

    """,

    'author': "Tritel",
    'website': "https://www.tritel.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Stock - Extended',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'security/ir_model_access.xml',
        'views/views.xml',
        'reports/variance_report.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],

    'application': True,
}