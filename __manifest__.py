{
    'name': 'Herbs Store Manager',
    'author': 'Sofic',
    'depends' : ['base', 'mail'],
    'license': 'LGPL-3',
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/order_readonly_views.xml',
        'views/order_views.xml',
        'views/menu.xml',
    ]
}