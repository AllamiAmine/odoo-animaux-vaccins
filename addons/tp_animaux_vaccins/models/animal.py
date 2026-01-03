from odoo import models, fields


class Animal(models.Model):
    _name = 'tp.animal'
    _description = 'Animal'

    name = fields.Char(string="Nom", required=True)
    type = fields.Selection([
        ('chien', 'Chien'),
        ('chat', 'Chat'),
        ('vache', 'Vache')
    ], string="Type")
    date_naissance = fields.Date(string="Date de naissance")
    vaccin_ids = fields.One2many(
        'tp.vaccin', 'animal_id', string="Vaccins"
    )
