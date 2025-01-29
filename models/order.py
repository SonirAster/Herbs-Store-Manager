from odoo import api, fields, models
from odoo.exceptions import ValidationError, MissingError


class HS_Order (models.Model) :
    _name = 'hs.order'
    _description = "herbs store customer's order"

    name = fields.Char(
        string='Title', 
        required=True,
        default='Order Name',
    )
    description = fields.Text(
        string='Description',
    )
    status = fields.Selection(
        string='Status',
        selection=[
            ('pending', 'Pending'),
            ('sent', "Sent"),
            ('canceled', "Canceled"),
            ('fulfilled', 'Fulfilled')
        ],
        default='pending',
        readonly=True
    )
    delivery_point = fields.Char(
        string='Delivery Point',
    )
    package_ids = fields.Many2many(
        'hs.stock', 
        string='Order',
        required=True
    )
    price = fields.Float(
        compute='_compute_total_price',
        string='Price ($)',
        default=0.00
    )
    customer_id = fields.Many2one(
        'hs.customer',
        string='Customer',
        required=True
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
        default='not urgent'
    )
    # Calculating total price of the order 
    @api.depends("package_ids")
    def _compute_total_price(self):
        for order in self:
            order.price = 0.00
            for item in order.package_ids:
                order.price += item.price
    # Fulfill the order
    def action_fulfill_order(self):
        for item in self:
            item.status = "fulfilled"
        return True
    # Send_order_action the order
    def action_send_order(self):
        for item in self:
            item.status = "sent"
        return True
    # Cancel_order_action the order
    def action_cancel_order(self):
        for item in self:
            item.status = "canceled"
        #raise ValidationError(('You can not do that.'))
        return True



