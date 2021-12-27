from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = "account.payment"


    def print_withholding_voucher(self):
        return self.env.ref('l10n_ar_account_withholding.action_report_withholding_certificate').report_action(self)