from odoo import fields, models

class Crysec_Course(models.Model):
    _name = 'crysec.course'
    _description = 'Main entity for Crysec Security Courses addon'
    name = fields.Char('Name', required=True, help='Course name')
    description = fields.Char('Description', required=True, help='Course description')
    image = fields.Image('Image', max_width=600, max_height=600)
    price = fields.Float('Price')