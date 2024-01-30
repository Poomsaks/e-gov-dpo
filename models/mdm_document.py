from odoo import models, fields


class MDMDocument(models.Model):
    _name = 'mdm.document'
    _description = 'รายละเอียดเอกสาร'
    _rec_name = 'name'

    image = fields.Binary(string='รูปภาพ', store=True, readonly=False)
    name = fields.Char(string='ชื่อหัวข้อ', required=False)
    name_create_id = fields.Many2one(comodel_name='res.partner', string='ผู้สร้าง', required=False)
    status = fields.Boolean(string='สถานะ', required=False, default=True)
    inspector_id = fields.Many2one(comodel_name='res.partner', string='ผู้ตรวจสอบ', required=False)
    document_status = fields.Selection(string="การตรวจ",
                                       selection=[('0', 'Draft'),
                                                  ('1', 'Submit'),
                                                  ('2', 'Approve'),
                                                  ('3', 'Reject'),
                                                  ('4', 'Complete')],
                                       required=False, defaul='0')
    doc_detail_ids = fields.One2many(comodel_name='mdt.doc.detail', inverse_name='document_id',
                                     string='รายละเอียดเอกสาร', required=False)


class MDTDocDetail(models.Model):
    _name = 'mdt.doc.detail'
    _description = 'Detail document'

    document_id = fields.Many2one(comodel_name='mdm.document', string='รหัสหัวข้อ', required=False)
    detail_no = fields.Char(string='เลขหน้า', required=False)
    doc_detail = fields.Text(string="เนื้อหาเอกสาร", required=False)
