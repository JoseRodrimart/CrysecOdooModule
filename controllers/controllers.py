import json
from odoo import http
from odoo.http import request

class CrysecControllers(http.Controller):

    @http.route('/course', auth='public', type='json', csrf=False)
    def courses(self):
        output = {
            'results':{
                'code':200,
                'message':'OK'
            }
        }
        #courses = request.env['crysec.course'].sudo().search([])
        return json.dumps(output) #courses.read(['name'])
    
    @http.route('/hello', auth='public', website=True)
    def courses(self):
        return "hello world"

    @http.route('/courses', auth='public', website=True, csrf=False)
    def courses(self):
        courses = request.env['crysec.course'].sudo().search([])
        return "hello world"