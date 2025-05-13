from odoo import api,fields,models


class ResPartner(models.Model):
    """add a selection field to the inherited form view of res.partner"""
    _inherit = "res.partner"
    _description = "res partner"

    purchase_limit = fields.Boolean(string="Activate Purchase Limit")
    amount = fields.Float(string="Limit amount")

    @api.model
    def _load_pos_data_fields(self, config_id):
        result = super()._load_pos_data_fields(config_id)
        result += ['amount']
        return result
