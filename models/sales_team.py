from odoo import models, fields, api

class SalesTeam(models.Model):
    _name = "sales.team"
    _description = 'crm_sales.sales.team'

    name = fields.Char("Sales Team Name")
    quotation = fields.Boolean("Quotations")
    pipeline = fields.Boolean(string="Pipeline")

    email = fields.Char("Email Alias")
    accept_email = fields.Selection([
        ('public', 'Everyone'),
        ('private', 'No one')
    ], string="Accept Emails From", default='everyone')

    invoice_target = fields.Float("Invoicing Target")
    monthly_sales_id = fields.One2many("monthly.sales", "sales_team", string="Monthly Sales List")


