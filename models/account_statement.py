from odoo import models, fields

class KuzeyAccountStatement(models.Model):
    _name = 'kuzey.account.statement'
    _description = 'Kuzey Account Statement'

    name = fields.Char(string="Ad")
