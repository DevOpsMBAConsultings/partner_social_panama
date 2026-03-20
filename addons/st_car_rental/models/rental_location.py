from odoo import models, fields, api

class RentalLocation(models.Model):
    _name = 'rental.location'
    _description = 'Car Rental Location'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(string='Location Name', required=True, translate=True)
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)
    parent_id = fields.Many2one('rental.location', string='Parent Location', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True, unaccent=False)
    child_ids = fields.One2many('rental.location', 'parent_id', string='Sub-Locations')
    
    type = fields.Selection([
        ('country', 'Country'),
        ('region', 'Region/State'),
        ('city', 'City'),
        ('branch', 'Branch/Parking'),
    ], string='Location Type', default='branch', required=True)

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    
    # Address details (for branches/parking)
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')

    latitude = fields.Float(string='Geo Latitude', digits=(10, 7))
    longitude = fields.Float(string='Geo Longitude', digits=(10, 7))

    active = fields.Boolean(default=True)

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for location in self:
            if location.parent_id:
                location.complete_name = '%s / %s' % (location.parent_id.complete_name, location.name)
            else:
                location.complete_name = location.name

    @api.constrains('parent_id')
    def _check_location_recursion(self):
        if not self._check_recursion():
            raise odoo.exceptions.ValidationError('You cannot create recursive locations.')
