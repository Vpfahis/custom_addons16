{
    'name': "Website Sale Reordering",
    'version': '16.0.1.0.0',
    'depends': ['website_sale', 'sale', 'portal'],
    'author': "Fahis",
    'category': 'My Category',
    'description': """
    A module to reorder in website from the users saleorder history.
    """,
    'data': [
        'views/website_sale_order_reorder_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
