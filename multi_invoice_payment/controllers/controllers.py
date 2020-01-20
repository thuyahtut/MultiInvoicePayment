# -*- coding: utf-8 -*-
from odoo import http

# class MultiInvoicePayment(http.Controller):
#     @http.route('/multi_invoice_payment/multi_invoice_payment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/multi_invoice_payment/multi_invoice_payment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('multi_invoice_payment.listing', {
#             'root': '/multi_invoice_payment/multi_invoice_payment',
#             'objects': http.request.env['multi_invoice_payment.multi_invoice_payment'].search([]),
#         })

#     @http.route('/multi_invoice_payment/multi_invoice_payment/objects/<model("multi_invoice_payment.multi_invoice_payment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('multi_invoice_payment.object', {
#             'object': obj
#         })