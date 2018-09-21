# -*- coding: utf-8 -*-

from openerp import fields, models, api


class ResPartner(models.Model):

    _inherit = 'res.partner'
    
    parking_card = fields.Char("Tarjeta de parking")
    porcentaje_parking = fields.Float("Porcentaje Parking")
    plazas_ids = fields.One2many(comodel_name='parking.place',inverse_name='cliente_id',string='Plazas de Parking')
        
    
    
    
    
    
    