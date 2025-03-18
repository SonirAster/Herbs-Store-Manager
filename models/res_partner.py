from odoo import api, fields, models


class Res_Partner (models.Model) :
    _inherit = 'res.partner'
    
    active_order_ids = fields.One2many(
        'hs.order', 'customer_id',
        string='Active Orders'
    )
    active_order_count = fields.Integer(
        string='Orders Count',
        compute='_compute_active_order_count',
    )

    @api.depends('active_order_ids')
    def _compute_active_order_count(self):
        order_count = self.env['hs.order'].search_count([('customer_id', '=', self.id)])
        self.active_order_count = order_count
    
    def delete_order(self):
        for rec in self:
            rec.active_order_ids.unlink()