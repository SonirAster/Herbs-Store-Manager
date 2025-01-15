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


