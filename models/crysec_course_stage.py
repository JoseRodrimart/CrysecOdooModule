from odoo import fields, models

class CrysecStage(models.Model):
    _name = 'crysec.course.stage'
    _order = 'sequence,name'

    name = fields.Char()
    sequence = fields.Integer()
    fold = fields.Boolean()
    course_stage = fields.Selection(
        [('inPreparation', 'In preparation'),
        ('openReservations', 'Reservations opened'),
        ('started', 'Already started'),
        ('completed','Completed'),
        ('cancelled', 'Cancelled')]
        ,'Stage', default="inPreparation")