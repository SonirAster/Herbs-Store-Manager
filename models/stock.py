from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HS_stock (models.Model) :
    _name = 'hs.stock'
    _description = 'herbs store prodicts list'

    name = fields.Char(
        string = 'Title', 
        required = True
    )
    description = fields.Text(
        string = 'Description'
    )
    properties = fields.Text(
        string = 'Propeties'
    )
    quantity = fields.Integer(
        string = 'Quantity'
    )
    price = fields.Float(
        string = 'Price',
        required = True,
        default = 0.00,
        help = 'how much the item shall cost'
    )
    cost = fields.Float(
        string = 'Cost',
        required = True,
        default = 0.00,
        help = 'actual price of the item'
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "A product with the same name already exists."),
    ]
    # нужно чтобы после оформления заказа из кол-ва вычитывался проданныц товар

    @api.constrains('price', 'cost', 'quantity')
    def _check_price(self):
        for rec in self:
            if rec.price < 0.00: raise ValidationError(f'The price cannot negative!')
            if rec.cost < 0.00: raise ValidationError(f'The cost cannot negative!')
            if rec.quantity < 0.00: raise ValidationError(f'The quantity cannot negative!')
