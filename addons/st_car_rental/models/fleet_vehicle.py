# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    is_rentable = fields.Boolean(string='Is Rentable', default=True, help='Check if this vehicle can be rented.')
    rental_rate_id = fields.Many2one('rental.rate', string='Default Rental Rate')
    rental_status = fields.Selection([
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('rented', 'Rented'),
        ('maintenance', 'In Maintenance')
    ], string='Rental Status', default='available')

    # Links to RMS Enhancements
    current_location_id = fields.Many2one(
        'rental.location', string='Current Location',
        domain=[('type', '=', 'branch')])
    
    supplier_id = fields.Many2one(
        'res.partner', string='Supplier / Owner',
        help="Used if the vehicle belongs to a third-party supplier (Multi-Supplier Mode).")

    # Optional accessories (SIM cards, Airport Pickup) that can be cross-sold during booking
    accessory_product_ids = fields.Many2many(
        'product.product', 
        string="Optional Accessories", 
        domain=[('sale_ok', '=', True)]
    )

    rental_order_ids = fields.One2many('sale.order', 'vehicle_id', string='Rental Orders')

    def action_view_rentals(self):
        self.ensure_one()
        return {
            'name': 'Rentals',
            'view_mode': 'list,form',
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
            'domain': [('vehicle_id', '=', self.id)],
            'context': {'default_vehicle_id': self.id},
        }
