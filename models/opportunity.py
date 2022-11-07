from odoo import models, fields, api


class Opportunity(models.Model):
    _name = 'opportunity'

    name = fields.Char("opportunity")
    expected_revenue = fields.Float(string="Expected Revenue")
    probability = fields.Float("Probability")

    # customer_id = fields.Many2one("customer", string="Customer Name")
    # customer_email = fields.Text(related="customer_id.email", string="Customer Email")
    # customer_phone = fields.Text(related="customer_id.phone", string="Customer Phone")
    sales_team = fields.Many2one("sales.team", string="Sales Team")
    expected_closing = fields.Date(string="Expected Closing", default=fields.Date.today())
