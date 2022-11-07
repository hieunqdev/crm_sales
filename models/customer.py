from odoo import models, fields, api

class Customer(models.Model):
    _name = 'customer'

    name = fields.Char("Name")
    phone = fields.Char("Phone")
    email = fields.Char("Email")
