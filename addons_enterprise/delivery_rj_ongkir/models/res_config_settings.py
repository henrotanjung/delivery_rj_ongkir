
from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    module_delivery_rj_ongkir = fields.Boolean("Raja Ongkir")