from odoo import api, fields, models


class Res_Partner (models.Model) :
    # _name = 'hs.customer'
    # _description = 'herbs store customers'
    _inherit = 'res.partner'
    
    # name = fields.Char(
    #     string='Customer',
    #     required=True
    # )
    # location = fields.Char(
    #     string='Located in'
    # )
    ddd = fields.Char(default='DD')
    active_order_ids = fields.One2many(
        'hs.order', 'customer_id',
        string='Active Orders'
    )
    active_order_count = fields.Integer(
        string='Orders Count',
        compute='_compute_active_order_count',
    )
    def delete_order(self):
        for rec in self:
            rec.active_order_ids.unlink()

    @api.depends('active_order_ids')
    def _compute_active_order_count(self):
        #COUNT ALL ORDERS OF CURRENT RECORD
        order_count = self.env['hs.order'].search_count([('customer_id', '=', self.id)])
        self.active_order_count = order_count
        #order_data = self.env['hs.order'].sudo()._read_group([('order_id', '=', self.id)])
        