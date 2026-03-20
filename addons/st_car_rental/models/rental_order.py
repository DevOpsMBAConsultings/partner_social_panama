# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_rental = fields.Boolean(string='Is Rental', default=False)
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', domain=[('is_rentable', '=', True)])
    
    pickup_date = fields.Datetime(string="Pick-up Date")
    return_date = fields.Datetime(string="Return Date")
    duration_days = fields.Integer(string="Duration (Days)", compute="_compute_duration", store=True)
    duration_hours = fields.Float(string="Duration (Hours)", compute="_compute_duration", store=True)

    pickup_location_id = fields.Many2one(
        'rental.location', string="Pick-up Location",
        domain=[('type', '=', 'branch')])
    return_location_id = fields.Many2one(
        'rental.location', string="Return Location",
        domain=[('type', '=', 'branch')])

    inspection_ids = fields.One2many('rental.inspection', 'order_id', string="Inspections")
    fine_ids = fields.One2many('rental.fine', 'order_id', string='Traffic Fines')

    @api.depends('pickup_date', 'return_date')
    def _compute_duration(self):
        for order in self:
            if order.pickup_date and order.return_date:
                delta = order.return_date - order.pickup_date
                order.duration_days = delta.days + (1 if delta.seconds > 0 else 0)
                order.duration_hours = delta.total_seconds() / 3600.0
            else:
                order.duration_days = 0
                order.duration_hours = 0.0

    @api.onchange('vehicle_id', 'pickup_date', 'return_date')
    def _onchange_rental_pricing(self):
        if self.is_rental and self.vehicle_id:
            if not self.vehicle_id.is_rentable:
                return {'warning': {'title': _('Invalid Vehicle'), 'message': _('This vehicle is not marked as rentable.')}}
            if self.vehicle_id.rental_status == 'maintenance':
                 return {'warning': {'title': _('Vehicle in Maintenance'), 'message': _('This vehicle is currently in maintenance and may not be available.')}}

            if self.vehicle_id.rental_rate_id:
                rate = self.vehicle_id.rental_rate_id
                
                # Default to daily rate logic
                unit_price = rate.daily_rate
                quantity = self.duration_days

                # Determine best tier based on duration
                if self.duration_days >= 30 and rate.monthly_rate:
                    unit_price = rate.monthly_rate / 30
                elif self.duration_days >= 14 and rate.biweekly_rate:
                    unit_price = rate.biweekly_rate / 14
                elif self.duration_days >= 7 and rate.weekly_rate:
                    unit_price = rate.weekly_rate / 7
                elif self.duration_hours > 0 and self.duration_hours < 24 and rate.hourly_rate:
                    unit_price = rate.hourly_rate
                    quantity = self.duration_hours

                if not self.order_line:
                    self.order_line = [(0, 0, {
                        'name': _('Rental of %s') % self.vehicle_id.display_name,
                        'product_uom_qty': quantity,
                        'price_unit': unit_price,
                    })]
                else:
                    for line in self.order_line:
                        line.product_uom_qty = quantity
                        line.price_unit = unit_price

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.is_rental and order.vehicle_id:
                order.vehicle_id.rental_status = 'reserved'
        return res

    def action_rental_pickup(self):
        self.ensure_one()
        if self.vehicle_id:
            self.vehicle_id.rental_status = 'rented'
            # Could trigger creation of 'Out' inspection here
            return {
                'name': _('New Inspection (Pickup)'),
                'type': 'ir.actions.act_window',
                'res_model': 'rental.inspection',
                'view_mode': 'form',
                'context': {
                    'default_order_id': self.id,
                    'default_type': 'out',
                },
                'target': 'new',
            }

    def action_rental_return(self):
        self.ensure_one()
        if self.vehicle_id:
            self.vehicle_id.rental_status = 'available'
            # Trigger 'In' inspection
            return {
                'name': _('New Inspection (Return)'),
                'type': 'ir.actions.act_window',
                'res_model': 'rental.inspection',
                'view_mode': 'form',
                'context': {
                    'default_order_id': self.id,
                    'default_type': 'in',
                },
                'target': 'new',
            }
