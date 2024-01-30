# -*- coding: utf-8 -*-
import base64
import json

from odoo import http
from odoo.http import request
from .con_check_role import ConCheckRole
from .config_database import ConfigDatabase


class ConBusiness(http.Controller):

    @http.route('/api/add_document', type='json', auth='user')
    def add_document(self, **post):
        data_model = request.env['mdm.document'].sudo().search([])
        data_create = data_model.create({
            'name': post.get('name'),
            'name_create_id': post.get('name_create_id'),
            'document_status': post.get('document_status'),
            'inspector_id': post.get('inspector_id'),
        })
        data = {'status': 200, 'response': data_create.id, 'message': 'success'}
        return json.dumps(data)

    @http.route('/api/add_document_detail', type='json', auth='user')
    def add_document_detail(self, **post):
        data_model = request.env['mdm.document'].sudo().search([('id', '=', post.get('id'))])
        if data_model:
            doc_detail = []
            if post.get('doc_detail_ids'):
                detail_day_data = json.loads(json.dumps(post.get('doc_detail_ids')))
                for rec in detail_day_data:
                    if rec.get('detail_id'):
                        doc_detail.append((1, rec.get('detail_id'), {
                            'document_id': data_model.id,
                            'detail_no': rec.get('detail_no'),
                            'doc_detail': rec.get('doc_detail'),
                        }))
                    else:
                        doc_detail.append((0, 0, {
                            'document_id': data_model.id,
                            'detail_no': rec.get('detail_no'),
                            'doc_detail': rec.get('doc_detail'),
                        }))
            data_model.write({
                'doc_detail_ids': doc_detail,
            })
            data = {'status': 200, 'response': data_model.id, 'message': 'success'}
            return json.dumps(data)

        data = {'status': 200, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
        return json.dumps(data)

    @http.route('/api/get_document_search', type='json', auth='none')
    def get_document_search(self, **post):
        request.session.db = ConfigDatabase.database
        search_param = []
        con_check_role = ConCheckRole()
        if post.get('id'):
            search_param.append(('id', '=', post.get('id')))
        if post.get('partner_id'):
            result = con_check_role.check_role(post.get('partner_id'))
            if result == "ผู้รับคำร้อง":
                search_param.append(('document_status', 'in', ['0', '2', '3', '4']))
            if result == "ผู้อนุมัติ":
                search_param.append(('document_status', '=', '1'))
        if search_param:  # ตรวจสอบว่ามีเงื่อนไขการค้นหาหรือไม่
            data_info = request.env['mdm.document'].sudo().search(search_param)
        else:
            # กรณีที่ไม่มีเงื่อนไขการค้นหา
            data_info = request.env['mdm.document'].sudo().search([])

        if data_info:
            data_s = []
            for rec in data_info:
                vals = {
                    'id': rec.id,
                    'name': rec.name or "",
                    'create_date': rec.create_date or "",
                    'name_create_id': rec.name_create_id.id or "",
                    'name_create_name': rec.name_create_id.name or "",
                    'status': rec.status or "",
                    'inspector_id': rec.inspector_id.id or "",
                    'inspector_name': rec.inspector_id.name or "",
                    'document_status': rec.document_status or "",
                }
                data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data

    @http.route('/api/get_document_for_detail_by_id', type='json', auth='none')
    def get_document_for_detail_by_id(self, **post):
        request.session.db = ConfigDatabase.database
        data_info = request.env['mdm.document'].sudo().search([('id', '=', post.get('id'))])
        if data_info:
            data_s = []
            for rec in data_info:
                vals = {
                    'id': rec.id,
                    'name': rec.name or "",
                    'name_create_id': rec.name_create_id.id or "",
                    'name_create_name': rec.name_create_id.name or "",
                    'status': rec.status or "",
                    'inspector_id': rec.inspector_id.id or "",
                    'inspector_name': rec.inspector_id.name or "",
                    'document_status': rec.document_status or "",
                    'doc_detail_ids': [{'id': record.id,
                                        'detail_no': record.detail_no,
                                        'doc_detail': record.doc_detail,
                                        }
                                       for record in rec.doc_detail_ids],
                }
                data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data

    @http.route('/api/get_document_for_detail', type='json', auth='none')
    def get_document_for_detail(self, **post):
        request.session.db = ConfigDatabase.database
        data_info = request.env['mdm.document'].sudo().search([])
        if data_info:
            data_s = []
            for rec in data_info:
                vals = {
                    'id': rec.id,
                    'name': rec.name or "",
                    'name_create_id': rec.name_create_id.id or "",
                    'name_create_name': rec.name_create_id.name or "",
                    'status': rec.status or "",
                    'inspector_id': rec.inspector_id.id or "",
                    'inspector_name': rec.inspector_id.name or "",
                    'document_status': rec.document_status or "",
                    'doc_detail_ids': [{'id': record.id,
                                        'detail_no': record.detail_no,
                                        'doc_detail': record.doc_detail,
                                        }
                                       for record in rec.doc_detail_ids],
                }
                data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data

    @http.route('/api/update_document', type='json', auth='user')
    def update_document(self, **post):
        data_model = request.env['mdm.document'].sudo().search([('id', '=', post.get('id'))])
        if data_model:
            doc_detail = []
            if post.get('doc_detail_ids'):
                inviters_append_data = json.loads(json.dumps(post.get('doc_detail_ids')))
                for rec in inviters_append_data:
                    if rec.get('detail_id'):
                        doc_detail.append((1, rec.get('detail_id'), {
                            'document_id': post.get('id'),
                            'detail_no': rec.get('detail_no'),
                            'doc_detail': rec.get('doc_detail')
                        }))
                    else:
                        doc_detail.append((0, 0, {
                            'document_id': post.get('id'),
                            'detail_no': rec.get('detail_no'),
                            'doc_detail': rec.get('doc_detail')
                        }))

            data_model.write({
                'name': post.get('name', data_model.name),
                'name_create_id': post.get('name_create_id', data_model.name_create_id.id),
                'status': post.get('status', data_model.status),
                'inspector_id': post.get('inspector_id', data_model.inspector_id.id),
                'document_status': post.get('document_status', data_model.document_status),
                'doc_detail_ids': doc_detail
            })
            data = {'status': 200, 'response': data_model.id, 'message': 'success'}
            return json.dumps(data)

    # @http.route('/api/delete_document', type='json', auth='user')
    # def delete_document(self, **post):
    #     data_model = request.env['mdm.document'].sudo().search([('id', '=', post.get('id'))])
    #     if data_model:
    #         data_model.unlink()
    #         data = {'status': 200, 'response': 'Delete success', 'message': 'success'}
    #         return json.dumps(data)
