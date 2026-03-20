# -*- coding: utf-8 -*-
from odoo import models, fields, api

class RentalInspection(models.Model):
    _name = 'rental.inspection'
    _description = 'Vehicle Rental Inspection'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: 'NEW')
    order_id = fields.Many2one('sale.order', string='Rental Order', required=True, ondelete='cascade')
    vehicle_id = fields.Many2one('fleet.vehicle', related='order_id.vehicle_id', store=True)
    
    type = fields.Selection([
        ('out', 'Pickup (Out)'),
        ('in', 'Return (In)'),
    ], string='Inspection Type', required=True, default='out')
    
    date = fields.Datetime(string='Inspection Date', default=fields.Datetime.now)
    inspector_id = fields.Many2one('res.users', string='Inspector', default=lambda self: self.env.user)
    
    # Checklist fields
    fuel_level = fields.Selection([
        ('empty', 'Empty'),
        ('quarter', '1/4'),
        ('half', '1/2'),
        ('three_quarter', '3/4'),
        ('full', 'Full'),
    ], string='Fuel Level', default='full')
    
    cleanliness = fields.Selection([
        ('poor', 'Poor'),
        ('fair', 'Fair'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    ], string='Cleanliness', default='excellent')
    
    notes = fields.Text(string='General Notes')
    
    # Photos (handled via attachments in Odoo usually, but we'll add a link)
    damage_description = fields.Text(string='Damage Description')

    @api.model
    def create(self, vals):
        if vals.get('name', 'NEW') == 'NEW':
            # Simplified sequence logic
            vals['name'] = self.env['ir.sequence'].next_by_code('rental.inspection') or 'INSP/%s' % fields.Datetime.now().strftime('%Y%m%d%H%M')
        return super(RentalInspection, self).create(vals)
