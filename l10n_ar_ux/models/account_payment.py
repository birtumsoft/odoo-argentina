from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    l10n_ar_partner_vat = fields.Char(related='partner_id.l10n_ar_vat', string='CUIT del destinatario')



class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    l10n_ar_partner_vat = fields.Char(related='partner_id.l10n_ar_vat', string='CUIT del destinatario')

    def _create_payment_vals_from_batch(self, batch_result):
        res = super(AccountPaymentRegister,self)._create_payment_vals_from_batch(batch_result)
        res.update({
            'l10n_ar_partner_vat': self.l10n_ar_partner_vat,
        })
        return res