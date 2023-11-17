# -*- coding: utf-8 -*-
{
    'name': "Invoice Post,Draft and Cancel from List View.",

    'summary': """
        Post your invoice/bill from list views and Multiple Cancel""",

    'description': """
        - Post, Reset to Draft, Register Payment and cancel customer invoice from list view
        - Post, Reset to Draft, Register Payment and cancel vendor bill from list view
    """,

    'author': "Naing Lynn Htun",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting/Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move.xml',
    ],
}
