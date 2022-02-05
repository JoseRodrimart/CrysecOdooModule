from odoo import fields, models

class Crysec_Course(models.Model):
    _name = 'crysec.course'
    _description = 'Main entity for Crysec Security Courses addon'

    #Here we set the current stage of each Course
    state = fields.Selection([
        ('inPreparation', 'In preparation'),
        ('openReservations', 'Reservations opened'),
        ('started', 'Already started'),
        ('Canceled', 'canceled')
    ])

    # With this field, odoo knows the current currency (Dollars, Euros, etc.)
    currency_id = fields.Many2one('res.currency', help='Currency') 

    name = fields.Char('Name', required=True, help='Course name')
    description = fields.Char('Description', required=True, help='Course description')
    image = fields.Image('Image', max_width=600, max_height=600, help='Associated image')
    price = fields.Monetary('Price', help='Price of the whole course')
    teachers_id = fields.Many2one('res.partner', help='Teachers')
    start_date = fields.Date('Start Date', help="The day the course will start")



    #Missing fields: Days until start (calculated) , Covered topics (Many2One with CybersecurityTopic), Maximum Seats, Available seats (calculated),