from odoo import fields,models


class ResPartner(models.Model):
    """add a selection field to the inherited form view of res.partner"""
    _inherit = "res.partner"
    _description = "res partner"

    purchase_limit = fields.Boolean(string="Activate Purchase Limit")
    amount = fields.Integer(string="set the amount")