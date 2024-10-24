from odoo import models, fields, api
import random

class DeveloperTag(models.Model):
    _name = 'developer.tag'
    _description = 'Developer Tag'
    _order = 'sequence,id'

    name = fields.Char(string="Nom", required=True)
    color = fields.Integer(string='Color Index', default=lambda self: random.randint(0, 11))  # Random color index
    sequence = fields.Integer(default=10)

    # @api.model
    # def create(self, vals):
    #     # Generate a random color index from 0 to 11
    #     vals['color'] = random.randint(0, 11)
    #     return super(DeveloperTag, self).create(vals)