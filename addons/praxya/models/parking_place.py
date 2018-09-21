# -*- coding: utf-8 -*-

from openerp import fields, models, api

class ParkingPlace(models.Model):

    _name='parking.place'
    
    cliente_id = fields.Many2one('res.partner','cliente')
    planta = fields.Selection([('uno', 'Primera'), ('dos', 'Segunda'),('tres', 'Tercera')], 'Planta ')
    plaza = fields.Char('Plaza') 