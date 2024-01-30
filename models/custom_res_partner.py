from odoo import models, fields


class CustomResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'CustomResPartner'

    position_id = fields.Many2one(comodel_name='mdm.position', string='ตำแหน่ง', required=False)
    username = fields.Char(string='User_name', required=False)
    password = fields.Char(string='Password', required=False)
    card_number_id = fields.Char(string='หมายเลขบัตรประชาชน', required=False)
    relation_status = fields.Selection(string="การตรวจ",
                                       selection=[('0', 'ผู้ป่วย/ผู้ใช้งาน/'),
                                                  ('1', 'เจ้าหน้าที่/ผู้สมัครงาน'),
                                                  ('2', 'ผู้สมัครงาน'),
                                                  ('3', 'คู่สัญญา/ผู้รับเหมา'),
                                                  ('4', 'ผู้ติดต่อ'),
                                                  ('5', 'อื่นๆ (โปรดระบุ)')],
                                       required=False, default='0')
    relation_detail = fields.Char(string='รายละเอียด', required=False)

    document_type_1 = fields.Char(string="ประเภทเอกสาร", required=False, )
    document_name_1 = fields.Char(string="ชื่อเอกสาร", required=False, )
    document_attach_1 = fields.Binary(string="เอกสาร", attachment=True)

    document_type_2 = fields.Char(string="ประเภทเอกสาร", required=False, )
    document_name_2 = fields.Char(string="ชื่อเอกสาร", required=False, )
    document_attach_2 = fields.Binary(string="เอกสาร", attachment=True)

    document_type_3 = fields.Char(string="ประเภทเอกสาร", required=False, )
    document_name_3 = fields.Char(string="ชื่อเอกสาร", required=False, )
    document_attach_3 = fields.Binary(string="เอกสาร", attachment=True)
