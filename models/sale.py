# -*- coding: utf-8 -*-
# Part of TigernixERP. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # def _get_rj_ongkir_service_types(self):
    #     return self.env['delivery.carrier']._get_rj_ongkir_service_types()

    def _get_rj_ongkir_service_types(self):
        datas = self.env['res.partner'].search([('category_id', 'in', [1, 2, 3])])
        print (datas)
        print ('datasssssssssssssssss')
        list_type = []
        for data in datas:
            list_type.append((data.vat, data.name))

        return list_type

    def _get_rj_ongkir_account_code(self):
        return self.env['delivery.carrier']._get_rj_ongkir_account_code()

    rj_ongkir_service_account_code = fields.Selection(_get_rj_ongkir_account_code, string="Raja Ongkir Service Type")
    rj_ongkir_carrier_account = fields.Char(string='Carrier Account', copy=False)
    rj_ongkir_service_type = fields.Selection(_get_rj_ongkir_service_types, string="Raja Ongkir Service Type")
    # ups_bill_my_account = fields.Boolean(related='carrier_id.ups_bill_my_account', readonly=True)

    # @api.onchange('rj_ongkir_service_account_code')
    # def onchange_rj_ongkir_service_account_code(self):
        
    #     code = [
    #         ('OKE', 'Ongkos Kirim Ekonomis (jne)'),
    #         ('REG', 'Layanan Reguler (jne, tiki)'),
    #         ('SPS', 'Super Speed (jne)'),
    #         ('YES', 'Yakin Esok Sampai (jne)'),
    #         ('ECO', 'Economi Service (tiki)'),
    #         ('ONS', 'Over Night Service (tiki)'),
    #         ('Paket Kilat Khusus', 'PAKET KILAT KHUSUS (POS)'),
    #         ('others', 'Others'),
            
    #     ]
        # self.ups_service_type = self.carrier_id.ups_default_service_type

    # @api.onchange('carrier_id')
    # def onchange_carrier_id(self):
    #     if self.state in ('draft', 'sent'):
    #         self.delivery_price = 0.0
    #         self.delivery_rating_success = False
    #         self.delivery_message = False
