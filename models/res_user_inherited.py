from odoo import models, fields

class res_users(models.Model):

    _inherit = 'res.users'
    courses_ids = fields.Many2many('crysec.course', string='courses') 

    