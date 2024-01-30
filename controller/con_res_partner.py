# -*- coding: utf-8 -*-
import base64
import json

from odoo import http
from odoo.http import request
from .con_check_role import ConCheckRole
from .config_database import ConfigDatabase


class ConResPartNer(http.Controller):

    @http.route('/api/add_member', type='json', auth='none')
    def add_member(self, **post):
        request.session.db = ConfigDatabase.database
        data_model = request.env['res.partner'].sudo().search([])
        data_create = data_model.create({
            'name': post.get('name'),
            'phone': post.get('phone'),
            'email': post.get('email'),
            'position_id': 3,

            'username': post.get('username'),
            'password': post.get('password'),

            'card_number_id': post.get('card_number_id'),
            'relation_status': post.get('relation_status'),
            'relation_detail': post.get('relation_detail'),

            'document_type_1': post.get('document_type_1'),
            'document_name_1': post.get('document_name_1'),
            'document_attach_1': post.get('document_attach_1'),

            'document_type_2': post.get('document_type_2'),
            'document_name_2': post.get('document_name_2'),
            'document_attach_2': post.get('document_attach_2'),

            'document_type_3': post.get('document_type_3'),
            'document_name_3': post.get('document_name_3'),
            'document_attach_3': post.get('document_attach_3'),
        })
        data = {'status': 200, 'response': data_create.id, 'message': 'success'}
        return json.dumps(data)

    @http.route('/api/get_partner', type='json', auth='none')
    def get_partner(self, **post):
        data_model = request.env['res.partner'].sudo().search([('position_id', '=', 2)])
        data_s = []
        for rec in data_model:
            vals = {
                'id': rec.id,
                'name': rec.name or "",
                'position_id': rec.position_id.id or "",
                'position_name': rec.position_id.name or "",
            }
            data_s.append(vals)
        data = {'status': 200, 'response': data_s, 'message': 'success'}
        return data

    @http.route('/api/get_partner_by_id', type='json', auth='none')
    def get_partner_by_id(self, **post):
        data_model = request.env['res.partner'].sudo().search([('id', '=', post.get('id'))])
        data_s = []
        for rec in data_model:
            vals = {
                'id': rec.id,
                'name': rec.name or "",
                'position_id': rec.position_id.id or "",
                'position_name': rec.position_id.name or "",
                'card_number_id': rec.card_number_id or "",
                'relation_status_name': dict(rec._fields['relation_status'].selection).get(rec.relation_status),
                'relation_status': rec.relation_status or None,
                'phone': rec.phone or "",
                'email': rec.email or "",
            }
            data_s.append(vals)
        data = {'status': 200, 'response': data_s, 'message': 'success'}
        return data
