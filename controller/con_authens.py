from odoo import http
from odoo.http import request
from .config_database import ConfigDatabase


class ConAuthens(http.Controller):

    @http.route('/api/authenticate_dpo', type='json', auth='none', csrf=False)
    def authenticate_dpo(self, **post):
        request.session.db = ConfigDatabase.database
        db_authen = ConfigDatabase.database
        partner_info = request.env['res.partner'].sudo().search(
            [('username', '=', post.get('username')), ('password', '=', post.get('password'))])
        if partner_info:
            request.session.authenticate(db_authen, ConfigDatabase.username, ConfigDatabase.password)
            data_s = []
            for rec in partner_info:
                vals = {
                    'partner_id': rec.id,
                    'name': partner_info.name or "",
                    'position_id': partner_info.position_id.id or "",
                }
                data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': "ไม่พบข้อมูล", 'message': 'error'}
            return data
