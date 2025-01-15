from odoo import api, fields, models


class HS_Order (models.Model) :
    _name = 'hs.order'
    _description = 'herbs store orders'

    title = fields.Char(
        string='Title', 
        required=True,
        default='Order Name',
    )
    _inherit = ['mail.thread']
    description = fields.Text(
        string='Description',
        tracking=True
    )
    expected_price = fields.Float(
        string='Expected Price', 
    )
    delivery_point = fields.Char(
        string='Delivery Point',
        tracking=True
    )
    package = fields.Text(
        string='Package',
        required=True,
        tracking=True
    )
    item = fields.Many2one(
        'hs.inventory',
        string='Item'
    )
    urgency = fields.Selection(
        string='Urgency',
        required=True,
        selection=[
            ('not urgent', 'Not Urgent'), 
            ('preferably sooner', 'Preferably Sooner'), 
            ('urgent', 'Urgent'), 
            ('very urgent', 'Very Urgent')
        ],
        tracking=True
    )
    customer = fields.Char(
        string='Customer',
        required=True,
        tracking=True
    )

