from odoo import models, fields, api

class KuzeyStatementWizard(models.TransientModel):
    _name = 'kuzey.statement.wizard'
    _description = 'Cari Ekstre Sihirbazı'

    partner_id = fields.Many2one('res.partner', string='Cari')
    date_from = fields.Date(string='Başlangıç Tarihi')
    date_to = fields.Date(string='Bitiş Tarihi')
    is_detailed = fields.Boolean(string='Detaylı Rapor')


    def generate_report(self):
        data = {
            'partner_id': self.partner_id.id,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'is_detailed': self.is_detailed,
        }
        return self.env.ref('kuzey_account_statement.action_statement_report_pdf').report_action(self, data=data)
