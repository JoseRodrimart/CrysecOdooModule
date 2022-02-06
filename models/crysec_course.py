from odoo import fields, models, api

class Crysec_Course(models.Model):
    _name = 'crysec.course'
    _description = 'Main entity for Crysec Security Courses addon'

    #Here we set the current stage of each Course and create an api function so the
    # kanban can know all the existing stages in our project

    @api.model
    def _read_group_stage_ids(self,stages,domain,order):
        stage_ids = self.env['crysec.course.stage'].search([])
        return stage_ids

    stage_id = fields.Many2one('crysec.course.stage', group_expand='_read_group_stage_ids')#, default=_default_rent_stage)

    # With this field, odoo knows the current currency (Dollars, Euros, etc.)
    currency_id = fields.Many2one('res.currency', string='Currency') 
    
    # Relation with the users
    teachers_id = fields.Many2one('res.partner')

    name = fields.Char('Name', required=True, help='Course name')
    description = fields.Char('Description', required=True, help='Course description')
    image = fields.Image('Image', max_width=600, max_height=600, help='Associated image')
    price = fields.Monetary('Price', help='Price of the whole course')
    start_date = fields.Date('Start Date', help="The day the course will start")

    #@api.model
    #def _default_rent_stage(self):
    #    Stage = self.env['crysec.course.stage']
    #    return Stage.search([], limit=1)

    #Missing fields: Days until start (calculated) , Covered topics (Many2One with CybersecurityTopic), Maximum Seats, Available seats (calculated),