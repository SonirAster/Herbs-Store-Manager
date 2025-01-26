from odoo import api, fields, models


class HS_Customer (models.Model) :
    _name = 'hs.customer'
    _description = 'herbs store customers'

    
    name = fields.Char(
        string='Customer',
        required=True
    )
    location = fields.Char(
        string='Located in'
    )
    active_orders = fields.One2many(
        'hs.order', 'customer_id',
        string='Active Orders'
    )
