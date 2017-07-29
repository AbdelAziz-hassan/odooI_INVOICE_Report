from openerp import fields, models, api
from openerp.tools import amount_to_text
from openerp.tools import amount_to_text_en

class sales_order_elements(models.Model):
    _inherit = "account.invoice"
    addationalInfo = fields.Text('Addational Information')
    total_text = fields.Char("Total Text", compute='_get_total_text')
    @api.multi
    def _get_total_text(self):
        """Use Odoo Tool to Get Total in Words"""
        for inv in self:
            inv.total_text = amount_to_text_en.amount_to_text(inv.amount_total,
                                            currency=inv.currency_id.name)
            


