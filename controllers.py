# -*- coding: utf-8 -*-
from openerp import http

# class Odoo-cylinders(http.Controller):
#     @http.route('/odoo-cylinders/odoo-cylinders/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-cylinders/odoo-cylinders/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-cylinders.listing', {
#             'root': '/odoo-cylinders/odoo-cylinders',
#             'objects': http.request.env['odoo-cylinders.odoo-cylinders'].search([]),
#         })

#     @http.route('/odoo-cylinders/odoo-cylinders/objects/<model("odoo-cylinders.odoo-cylinders"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-cylinders.object', {
#             'object': obj
#         })