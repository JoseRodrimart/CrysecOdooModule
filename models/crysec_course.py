from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class Crysec_Course(models.Model):
    _name = 'crysec.course'
    _description = 'Main entity for Crysec Security Courses addon'

    name = fields.Char('Name', required=True, help='Course name')

    description = fields.Char('Description', required=True, help='Course description')

    image = fields.Image('Image', max_width=600, max_height=600, help='Associated image', store=True)

    start_date = fields.Date('Start Date', help="The day the course will start", default = datetime.today())

    price = fields.Monetary('Price', required=True, help='Price of the whole course')

    stage_id = fields.Many2one('crysec.course.stage', group_expand='_read_group_stage_ids', default=lambda self: self.env['crysec.course.stage'].search([]))

    # With this field, odoo knows the current currency (Dollars, Euros, etc.)
    currency_id = fields.Many2one('res.currency', string='Currency') 
    
    # Relation with the teacher
    teachers_id = fields.Many2one('res.users', domain=lambda self: [("groups_id", "=", self.env.ref( "CybersecurityCourses.group_teacher" ).id)])

    # Relation with the topics
    topics_ids = fields.Many2many('crysec.course.topic', string='Topics')

    # Relation with the students
    students_ids = fields.Many2many('res.users', string='Students')
    maxSeats = fields.Integer('Total of seats', default=10)
    percentajeSeats = fields.Float(compute='_compute_percentajeSeats', string='percentajeSeats')

    #Creation override
    @api.model
    def create(self, vals):
        rec = super(Crysec_Course, self).create(vals)
        #print("DEBUG CASERO:"+vals.name)
        self.env['product.template'].create({'list_price': vals["price"], 'name': vals["name"], 'image_256':vals["image"], 'image_1024':vals["image"]})#, 'image':vals["image"]})
        self.env.cr.commit()
        return rec

    @api.model
    def _read_group_stage_ids(self,stages,domain,order):
        stage_ids = self.env['crysec.course.stage'].search([])
        return stage_ids

    @api.depends ('maxSeats')
    def _compute_percentajeSeats(self):
        for course in self:
            countOcuppiedSeats = len(course.students_ids)
            if(course.maxSeats == 0): course.percentajeSeats = 0
            else: course.percentajeSeats = ((countOcuppiedSeats * 100)/course.maxSeats)

    

    

    def complete(self):
        for record in self:
            if record.stage_id.id == 5:
                raise UserError('A cancelled course can´t be completed.')
                return False
        for x in self.env['crysec.course.stage'].search([]):
            if x.id == 4:
                for record in self:
                    record.stage_id = x
        return True

    def cancel(self):
        for record in self:
            if record.stage_id.id == 4:
                raise UserError('A Completed course can´t be cancelled.')
                return False
        for x in self.env['crysec.course.stage'].search([]):
            if x.id == 5:
                for record in self:
                    record.stage_id = x
        return True

    # Constraints
    _sql_contraints = [
        ('name_unique','UNIQUE(name)','The name must be unique')
    ]
    
    @api.constrains('maxSeats')
    def _check_seats(self):
        for record in self:
            if record.maxSeats <= 0:
                raise ValidationError("The number of seats must be higher than zero.")

    @api.constrains('students_ids')
    def _check_students_ids(self):
        for record in self:
            if len(record.students_ids) > record.maxSeats:
                raise ValidationError("The number of students cannot be greater than the number of places.")

    @api.constrains('start_date')
    def _check_start_date(self):
        for record in self:
            if record.start_date < datetime.today().date():
                raise ValidationError("The start date cannot be earlier than today.")

    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError("The price must be higher than zero.")
