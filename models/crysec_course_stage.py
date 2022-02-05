from odoo import fields, models

class LibraryRentStage(models.Model):
    _name = 'crysec.course.stage'
    _order = 'sequence,name'
    name = fields.Char()
    sequence = fields.Integer()
    fold = fields.Boolean()
    course_state = fields.Selection(
        [('inPreparation', 'In preparation'),
        ('openReservations', 'Reservations opened'),
        ('started', 'Already started'),
        ('completed','Completed'),
        ('Cancelled', 'cancelled')]
        ,'State', default="inPreparation")