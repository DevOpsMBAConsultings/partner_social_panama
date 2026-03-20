# -*- coding: utf-8 -*-
from odoo import models, fields, api

class RentalFine(models.Model):
    _name = 'rental.fine'
    _description = 'Rental Traffic Fine'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Fine Reference', required=True)
    order_id = fields.Many2one('sale.order', string='Rental Order', required=True)
    vehicle_id = fields.Many2one('fleet.vehicle', related='order_id.vehicle_id', store=True)
    date = fields.Date(string='Fine Date', default=fields.Date.context_today)
    
    amount = fields.Monetary(string='Fine Amount', required=True)
    currency_id = fields.Many2one('res.currency', related='order_id.currency_id')
    
    description = fields.Text(string='Description/Violation Details')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
        ('invoiced', 'Invoiced'),
    ], default='draft', string='Status', tracking=True)

    def action_confirm(self):
        self.write({'state': 'confirmed'})
