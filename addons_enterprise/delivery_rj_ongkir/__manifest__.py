# -*- coding: utf-8 -*-
# Part of TigernixERP. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Raja Ongkir',
    'version' : '1.0',
    'summary': 'Shipping Integration',
    'sequence': 100,
    'description': """
        Feature yang digunakan untuk integrasi pengiriman melalu API Raja Ongkir
    """,
    'category': 'Delivery',
    'website': '',
    'depends' : ['delivery'],
    'data': [
        # 'wizard/update_qty_view.xml',
        # 'reports/report.xml'
        # 'views/sale_views.xml'
        'views/res_config_settings_views.xml',
        'views/delivery_rj_ongkir_view.xml',
        'data/delivery_rj_ongkir_data.xml'
    ],    
    
    'installable': True,
    'application': False,
    'auto_install': False,
    
}
