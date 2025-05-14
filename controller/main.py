# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class POSLimitController(http.Controller):

    @http.route('/pos/update_purchase_limit_limit', type='json', auth='user')
    def update_purchase_limit_limit(self, partner_id, balance_amount):
        partner = request.env['res.partner'].browse(partner_id)
        if partner.purchase_limit:
            partner.balance_amount = balance_amount
        return True
