from odoo import models, fields


class Vaccin(models.Model):
    _name = 'tp.vaccin'
    _description = 'Vaccin'

    name = fields.Char(string="Nom du vaccin", required=True)
    date_vaccin = fields.Date(string="Date du vaccin")
    animal_id = fields.Many2one(
        'tp.animal', string="Animal", ondelete="cascade"
    )
