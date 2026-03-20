# -*- coding: utf-8 -*-
from odoo import models, fields, api

class RentalRate(models.Model):
    _name = 'rental.rate'
    _description = 'Rental Pricing Rate'
    _order = 'sequence, id'

    name = fields.Char(string='Rate Name', required=True)
    sequence = fields.Integer(default=10)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')

    daily_rate = fields.Monetary(string='Daily Rate', currency_field='currency_id', required=True)
    hourly_rate = fields.Monetary(string='Hourly Rate', currency_field='currency_id')
    weekly_rate = fields.Monetary(string='Weekly Rate', currency_field='currency_id')
    biweekly_rate = fields.Monetary(string='Bi-weekly Rate', currency_field='currency_id')
    monthly_rate = fields.Monetary(string='Monthly Rate', currency_field='currency_id')

    active = fields.Boolean(default=True)
    notes = fields.Text(string='Description/Terms')
