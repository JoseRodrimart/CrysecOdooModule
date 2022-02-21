from odoo import models, fields, api

class Crysec_course_topic(models.Model):
	_name = "crysec.course.topic"
	_description = "Topics for crysec cybersecurity courses"
	
	name = fields.Char('Topic', required=True)
	color = fields.Integer('Color')
	
	_sql_constraints = [ ('etiqueta_unique', 'UNIQUE(name)', 'The name must be unique.'),]
	