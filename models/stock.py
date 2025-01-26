from odoo import api, fields, models


class HS_stock (models.Model) :
    _name = 'hs.stock'
    _description = 'herbs store prodicts list'

    name = fields.Char(
        string='Title', 
        required=True
    )
    description = fields.Text(
        string='Description'
    )
    properties = fields.Text(
        string='Propeties'
    )
    quantity = fields.Float(
        string='Quantity(kg)'
    )
    price = fields.Float(
        string='Price',
        required=True,
        default = 0.00
    )
    cost = fields.Float(
        string='Price',
        required=True,
        default = 0.00
    )

    # нужно чтобы после оформления заказа из кол-ва вычитывался проданныц товар