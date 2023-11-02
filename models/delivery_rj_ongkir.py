# -*- coding: utf-8 -*-
# Part of TigernixERP. See LICENSE file for full copyright and licensing details.
from odoo import api, models, fields, _
from odoo.exceptions import UserError
from odoo.tools import pdf
import http.client

# from .ups_request import UPSRequest, Package
from .rj_ongkir_request import RjOngkirRequest, Package


class ProviderRjOngkir(models.Model):
    _inherit = 'delivery.carrier'

    def _get_rj_ongkir_service_types(self):
        
        return [
            ('OKE', 'Ongkos Kirim Ekonomis (jne)'),
            ('REG', 'Layanan Reguler (jne, tiki)'),
            ('SPS', 'Super Speed (jne)'),
            ('YES', 'Yakin Esok Sampai (jne)'),
            ('ECO', 'Economi Service (tiki)'),
            ('ONS', 'Over Night Service (tiki)'),
            ('Paket Kilat Khusus', 'PAKET KILAT KHUSUS (POS)'),
            ('others', 'Others'),
            
        ]
    
    def _get_rj_ongkir_account_code(self):
        return [
            ('jne', 'JNE'),
            ('pos', 'POS Indonesia'),
            ('tiki', 'Tiki'),
            
        ]

    delivery_type = fields.Selection(selection_add=[('rj_ongkir', "Raja Ongkir")])
    token = fields.Char(string='Token')
    conn = fields.Char(string='Conn')
    content_type = fields.Char(string='content-type')
    

    def rj_ongkir_rate_shipment(self, order):
        client = order.partner_id
        superself = self.sudo()
        srm = RjOngkirRequest()

        ResCurrency = self.env['res.currency']
        
        # packages = []
        total_qty = 0
        total_weight = 0
        for line in order.order_line.filtered(lambda line: not line.is_delivery):
            total_qty += line.product_uom_qty
            total_weight += line.product_id.weight * line.product_qty
        # print (total_weight, 'total weightttttttttttt')

        # packages.append(Package(self, total_weight))

        ### di remark untuk sementara 
        # check_value = srm.check_required_value(order.company_id.partner_id, order.warehouse_id.partner_id, order.partner_shipping_id, order=order)
        # if check_value:
        #     return {'success': False,
        #             'price': 0.0,
        #             'error_message': check_value,
        #             'warning_message': False}

        assert order.partner_id.city , 'City id cannot empty'
        address_city_id = order.partner_id.city
        
        headers = {
            'key': self.token,
            'content-type': "application/x-www-form-urlencoded"
            }
        result = srm.get_shipping_price(
            total_weight=total_weight, shipper=order.company_id.partner_id, ship_from=order.warehouse_id.partner_id,
            ship_to=address_city_id, shipper_carrier=order.rj_ongkir_service_account_code, service_type=order.rj_ongkir_service_type,
            headers=headers, conn= self.conn)
        
        result = dict(result)

        if result['rajaongkir']['status']['code'] != 200:
            return {'success': False,
                    'price': 0.0,
                    'error_message': 'errr',
                    'warning_message': False}

        quote_currency = ResCurrency.search([('name', '=', 'IDR')], limit=1)
        paket_type_costs = result['rajaongkir']['results'][0]['costs']
        price = 0
        for paket in paket_type_costs:     
            if order.rj_ongkir_service_type == paket['service']:
                price = quote_currency.compute(float(paket['cost'][0]['value']), order.currency_id)
        
        return {'success': True,
                'price': price,
                'error_message': False,
                'warning_message': False}
