# Car Rental Management System (Odoo 19)

Implement a comprehensive car rental management system for Odoo 19, inspired by RentlySoft RMS features.

## Tasks

- [x] **Planning & Research** [x]
    - [x] Analyze RentlySoft features
    - [x] Research Odoo 19 technical patterns via NotebookLM
    - [x] Define module structure and dependencies
- [ ] **Core Module Setup** [/]
    - [/] Create `st_car_rental` module manifest and basic structure
    - [ ] Define security groups and access rights
- [x] **Data Models Implementation** [x]
    - [x] Extend `fleet.vehicle` with rental metadata
    - [x] Create `rental.rate` for dynamic pricing
    - [x] Implement `rental.order` (extending `sale.order` or new model)
    - [x] Implement `rental.inspection` (In/Out checks)
    - [x] Implement `rental.fine` (Traffic fines management)
- [x] **Data Models Implementation (RMS Enhancements)** [x]
    - [x] Add `hourly_rate` & `biweekly_rate` to `rental.rate`
    - [x] Create `rental.location` model (hierarchical mapping)
    - [x] Link `vehicle_id` and `rental.order` to `rental.location`
- [x] **Business Logic Enhancements** [x]
    - [x] Hourly/Bi-weekly calculation logic in `rental.order`
    - [x] Multi-supplier support checks on `fleet.vehicle`
- [x] **Views & UI Enhancements (RMS)** [x]
    - [x] Create views and menu for `rental.location`
    - [x] Add new pricing tiers to `rental.rate` views
    - [x] Surface location fields on `rental.order` and `fleet.vehicle` views
- [x] **Website Integration (B2C E-commerce)** [x]
    - [x] Create Python controllers for `/rental/cars` and `/rental/book` routes
    - [x] Create QWeb templates for vehicle catalog and details page
    - [x] Add `website` module dependency in manifest
- [x] **Loyalty Program (Programa de Fidelidad)** [x]
    - [x] Add `loyalty` module dependency to `__manifest__.py`
    - [x] Update documentation to reflect native rewards and coupons support
- [x] **Service Bundling & Cross-Selling** [x]
    - [x] Add `accessory_product_ids` Many2many to `fleet.vehicle`
    - [x] Update frontend QWeb template to display accessory checkboxes
    - [x] Update `/rental/book` controller to generate extra `sale.order.line` items
- [x] **Views & UI (Initial)** [x]
    - [x] Main Menu structure & Rental Rates
    - [x] Extend Fleet and Sale views
    - [x] Inspection and Fine views
    - [x] Car Rental Dashboard (Kanban + Calendar)
- [x] **Business Logic (Initial)** [x]
    - [x] Automated rate calculation and status transitions
    - [x] Maintenance alerts integration
- [ ] **Verification** [/]
    - [ ] Test rental workflow: Booking -> Pick-up -> Inspection -> Return -> Invoicing
    - [ ] Verify fine tracking
    - [x] Verify RMS Enhancements (Locations, Tiers, Suppliers)
