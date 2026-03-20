from odoo import http, _
from odoo.http import request

class CarRentalController(http.Controller):

    @http.route(['/rental/cars'], type='http', auth="public", website=True)
    def rental_cars_list(self, **kwargs):
        """Displays all rentable vehicles on the website catalog."""
        branch_id = kwargs.get('branch_id')
        pickup_date = kwargs.get('pickup_date')
        return_date = kwargs.get('return_date')

        # Base Domain: Must be a rentable vehicle
        domain = [('is_rentable', '=', True)]
        
        if branch_id:
            domain.append(('current_location_id', '=', int(branch_id)))

        vehicles = request.env['fleet.vehicle'].sudo().search(domain)
        
        # Real-Time Inventory Check: Filter out vehicles already booked for these dates
        if pickup_date and return_date:
            overlapping_orders = request.env['sale.order'].sudo().search([
                ('is_rental', '=', True),
                ('state', 'in', ['sale', 'done']),
                ('vehicle_id', 'in', vehicles.ids),
                ('pickup_date', '<=', return_date),
                ('return_date', '>=', pickup_date)
            ])
            unavailable_vehicle_ids = overlapping_orders.mapped('vehicle_id.id')
            vehicles = vehicles.filtered(lambda v: v.id not in unavailable_vehicle_ids)

        # Load locations for the search/filter dropdown
        locations = request.env['rental.location'].sudo().search([('type', '=', 'branch')])

        values = {
            'vehicles': vehicles,
            'locations': locations,
            'search_branch_id': branch_id and int(branch_id) or False,
            'search_pickup': pickup_date or '',
            'search_return': return_date or '',
        }
        return request.render('st_car_rental.rental_cars_list_template', values)

    @http.route(['/rental/car/<model("fleet.vehicle"):vehicle>'], type='http', auth="public", website=True)
    def rental_car_detail(self, vehicle, **kwargs):
        """Displays details for a specific vehicle and the booking form."""
        if not vehicle.is_rentable:
            return request.redirect('/rental/cars')
            
        locations = request.env['rental.location'].sudo().search([('type', '=', 'branch')])
        
        values = {
            'vehicle': vehicle,
            'locations': locations,
            # Pass through search params to pre-fill the booking form
            'pickup_date': kwargs.get('pickup_date', ''),
            'return_date': kwargs.get('return_date', ''),
            'pickup_location_id': kwargs.get('pickup_location_id', ''),
            # We can pass error messages back if form validation fails
            'error': kwargs.get('error', ''),
        }
        return request.render('st_car_rental.rental_car_detail_template', values)

    @http.route(['/rental/book'], type='http', auth="public", website=True, methods=['POST'])
    def handle_rental_booking(self, **post):
        """Handles the form submission from the vehicle detail page."""
        vehicle_id = int(post.get('vehicle_id'))
        pickup_date = post.get('pickup_date')
        return_date = post.get('return_date')
        pickup_location_id = int(post.get('pickup_location_id'))
        return_location_id = int(post.get('return_location_id'))
        
        # Basic validation
        if not (pickup_date and return_date and pickup_location_id and return_location_id):
            return request.redirect('/rental/car/%s?error=missing_fields' % vehicle_id)

        # In a real B2C scenario, we'd find or create the partner (customer)
        # based on the logged in user or a guest checkout form.
        # For this MVP, we link to the current user's partner.
        partner = request.env.user.partner_id
        if request.env.user._is_public():
            # Fallback if guest checkout isn't fully implemented yet
            return request.redirect('/web/login?redirect=/rental/car/%s' % vehicle_id)

        # Create the Sale Order (Rental Order)
        order_vals = {
            'partner_id': partner.id,
            'vehicle_id': vehicle_id,
            'pickup_date': pickup_date,
            'return_date': return_date,
            'pickup_location_id': pickup_location_id,
            'return_location_id': return_location_id,
            'is_rental': True,
        }
        
        # Sudos used as website users might not have full creation rights yet before confirmation
        rental_order = request.env['sale.order'].sudo().create(order_vals)
        
        # Trigger the main rental pricing calculation
        rental_order._onchange_rental_pricing()

        # Handle Optional Accessories (Cross-Selling)
        accessory_ids = request.httprequest.form.getlist('accessory_ids')
        if accessory_ids:
            for acc_id in accessory_ids:
                request.env['sale.order.line'].sudo().create({
                    'order_id': rental_order.id,
                    'product_id': int(acc_id),
                    'product_uom_qty': 1,
                })

        # Redirect to the standard Odoo checkout/quotation view
        return request.redirect('/my/orders/%s' % rental_order.id)
