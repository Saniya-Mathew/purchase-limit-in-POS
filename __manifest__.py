{
        'name': "POS Purchase limit",
        'version': '1.0',
        'type': 'module',
        'depends': ['base','point_of_sale'],
        'author': "San",
        'category': 'Category',
        'description': """Set a purchase limit for a customer""",

        # data files always loaded at installation
    'data': [
        'views/res_partner.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

    # 'assets': {
    #     'point_of_sale._assets_pos': [
    #         'pos_purchase_limit/static/src/xml/product_screen.xml',
    #         'pos_purchase_limit/static/src/js/product_screen.js',
    #     ],
    # },
}