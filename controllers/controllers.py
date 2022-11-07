# -*- coding: utf-8 -*-
# from odoo import http


# class CrmSales(http.Controller):
#     @http.route('/crm_sales/crm_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_sales/crm_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_sales.listing', {
#             'root': '/crm_sales/crm_sales',
#             'objects': http.request.env['crm_sales.crm_sales'].search([]),
#         })

#     @http.route('/crm_sales/crm_sales/objects/<model("crm_sales.crm_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_sales.object', {
#             'object': obj
#         })
