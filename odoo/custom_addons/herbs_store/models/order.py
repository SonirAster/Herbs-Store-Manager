from odoo import api, fields, models


class Order (models.Model) :
    _name = 'hs.order'
    _description = 'herbs store orders'

    title = fields.Char(
        string='Title', 
        required=True,
        default='Order Name',
    )
    description = fields.Text(
        string='Description'
    )
    expected_price = fields.Float(
        string='Expected Price', 
    )
    urgency = fields.Selection(
        string='Urgency',
        required=True,
        selection=[
            ('not urgent', 'Not Urgent'), 
            ('preferably sooner', 'Preferably Sooner'), 
            ('urgent', 'Urgent'), 
            ('very urgent', 'Very Urgent')
        ]
    )
