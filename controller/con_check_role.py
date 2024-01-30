import json

from odoo import http
from odoo.http import request


class ConCheckRole():

    def check_role(self, id):
        role = ""
        data_model = request.env['res.partner'].sudo().search([('id', '=', id)])
        for rec in data_model:
            role = rec.position_id.name
        return role
