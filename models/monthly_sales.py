from odoo import models, fields, api

class MonthlySales(models.Model):
    _name = "monthly.sales"
    _sql_constraints = [
        ("check_january_sales", "CHECK(january_sales > 0)", "The expected price must be strictly positive"),
        ("check_february_sales", "CHECK(february_sales > 0)", "The expected price must be strictly positive"),
        ("check_march_sales", "CHECK(march_sales > 0)", "The expected price must be strictly positive"),
        ("check_april_sales", "CHECK(april_sales > 0)", "The expected price must be strictly positive"),
        ("check_may_sales", "CHECK(may_sales > 0)", "The expected price must be strictly positive"),
        ("check_june_sales", "CHECK(june_sales > 0)", "The expected price must be strictly positive"),
        ("check_july_sales", "CHECK(july_sales > 0)", "The expected price must be strictly positive"),
        ("check_august_sales", "CHECK(august_sales > 0)", "The expected price must be strictly positive"),
        ("check_september_sales", "CHECK(september_sales > 0)", "The expected price must be strictly positive"),
        ("check_october_sales", "CHECK(october_sales > 0)", "The expected price must be strictly positive"),
        ("check_november_sales", "CHECK(november_sales > 0)", "The expected price must be strictly positive"),
        ("check_december_sales", "CHECK(december_sales > 0)", "The expected price must be strictly positive"),
    ]

    january_sales = fields.Float("January Sales")
    february_sales = fields.Float("February Sales")
    march_sales = fields.Float("March Sales")
    april_sales = fields.Float("April Sales")
    may_sales = fields.Float("May Sales")
    june_sales= fields.Float("June Sales")
    july_sales = fields.Float("July Sales")
    august_sales = fields.Float("August Sales")
    september_sales = fields.Float("September Sales")
    october_sales = fields.Float("October Sales")
    november_sales = fields.Float("November Sales")
    december_sales = fields.Float("December Sales")

    sales_team = fields.Many2one("sales.team", string="Sales Team")

