from odoo import api, fields, models


class HS_Inventory (models.Model) :
    _name = 'hs.inventory'
    _description = 'herbs store inventory'
    _inherit = ['mail.thread']
    title = fields.Char(
        string='Title', 
        required=True,
        default='Inventory Item',
    )
    description = fields.Text(
        string='Description'
    )
    quantity = fields.Int(
        string='Quantity',
        tracking=True
    )
    note = fields.Text(
        string='Note',
        tracking=True
    )
