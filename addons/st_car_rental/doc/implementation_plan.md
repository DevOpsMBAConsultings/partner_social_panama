# Car Rental Management System (ST Car Rental)

Deliver a robust car rental solution (RMS) for Odoo 19, replicating core features of RentlySoft such as real-time fleet tracking, booking, digital inspections (In/Out), and fine management.

## User Review Required

> [!IMPORTANT]
> The module will use Odoo's native **Fleet** module for vehicle tracking and **Sale** for contracts.
> Custom data models will be introduced for Inspections and Fines to mimic RentlySoft's feature set.

## Proposed Changes

### [Core Model Extensions]

#### [MODIFY] [fleet.vehicle](file:///Users/brooks/Development/odoo-dev/addons/st_car_rental/models/fleet_vehicle.py)
- [NEW] Add `rental_rate_id` link to pricing table.
- [NEW] Add `is_rentable` toggle.
- [NEW] Link to `rental.inspection` history.
- [NEW] Optional `supplier_id` (res.partner) or native multi-company setups to support RMS Multi-Supplier mode.

### [New Rental Components]

#### [NEW] [rental.location](file:///Users/brooks/Development/odoo-dev/addons/st_car_rental/models/rental_location.py)
- Hierarchical location model (Country > Region > City > Parking/Branch).
- Address details and geolocation support.

#### [NEW] [rental.rate](file:///Users/brooks/Development/odoo-dev/addons/st_car_rental/models/rental_rate.py)
- Model for flexible pricing: **hourly**, daily, weekly, **bi-weekly**, and monthly rates.
- Seasonal rate adjustments.

#### [NEW] [rental.order](file:///Users/brooks/Development/odoo-dev/addons/st_car_rental/models/rental_order.py)
- Inherits from `sale.order`.
- Adds `pickup_date`, `return_date`, `pickup_location_id`, `return_location_id` (links to `rental.location`).
- Automatic calculation of rental days/hours and price based on hourly/daily/weekly/monthly tiers.
- Digital signature field for customer acceptance.

#### [NEW] [rental.inspection](file:///Users/brooks/Development/odoo-dev/addons/st_car_rental/models/rental_inspection.py)
- "In & Out" digital checklist (fuel level, damage, cleanliness).
- Photo attachments for proof of state before/after rental.

#### [NEW] [rental.fine](file:///Users/brooks/Development/odoo-dev/addons/st_car_rental/models/rental_fine.py)
- Tracking for traffic fines received during a rental period.
- Link to both the vehicle and the `rental.order`.

### [Website Booking Portal (B2C)]

#### [NEW] [controllers/main.py](file:///Users/brooks/Development/odoo-dev/addons/st_car_rental/controllers/main.py)
- `@http.route('/rental/cars')`: Displays available vehicles with filtering by location and date.
- `@http.route('/rental/book')`: Handles form submission to generate a `rental.order` from the web.

#### [NEW] [views/website_rental_templates.xml](file:///Users/brooks/Development/odoo-dev/addons/st_car_rental/views/website_rental_templates.xml)
- QWeb template for the vehicle catalog (`rental_cars_list`).
- QWeb template for the vehicle details and booking form (`rental_car_detail`).

### [Loyalty Program ("Programa de Fidelidad")]

#### Native Odoo Integration
- Because our `rental.order` inherently extends Odoo's core `sale.order`, we do **not** need to build a custom loyalty engine from scratch.
- We will add the standard Odoo **`loyalty`** module as a dependency in `__manifest__.py`.
- This instantly unlocks robust configurations for:
  - Reward points (e.g., "Earn 10 points per $1 spent on rentals").
  - Promotions & Coupons (e.g., "10% off weekend rentals").
  - Free upgrades or discounts redeemable directly on the web portal and backend sales order form.

### [UI / Views]

#### [NEW] [views/rental_dashboard_views.xml](file:///Users/brooks/Development/odoo-dev/addons/st_car_rental/views/rental_dashboard_views.xml)
- Kanban view for vehicles grouped by status (Available, Rented, Maintenance).
- Calendar view for rental bookings.

## Verification Plan

### Automated Tests
- `pytest` suite for:
    - Correct price calculation for different rental durations.
    - Vehicle status transition logic (Cannot rent if in maintenance).

### Manual Verification
- Execute full cycle:
    1. Create a rental order for a specific vehicle and date range.
    2. Perform "Out" inspection during pick-up.
    3. Register a dummy traffic fine.
    4. Perform "In" inspection on return.
    5. Finalize invoice including rental charge + fines.
