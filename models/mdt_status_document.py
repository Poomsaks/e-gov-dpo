from odoo import models, fields


class MDTStatusDocument(models.Model):
    _name = 'mdt.status.document'
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
    doc_detail_ids = fields.One2many(comodel_name='mdt.status.doc.detail', inverse_name='document_id',
                                     string='รายละเอียดเอกสาร', required=False)
    comment = fields.Text(string="หมายเหตุ", required=False, widget="html")
    detail = fields.Text(string="เหตุผลประกอบคําร้อง", required=False, widget="html")
    relation_status = fields.Selection(string="การตรวจ",
                                       selection=[('0', 'เพิกถอนความยินยอม'),
                                                  ('1',
                                                   'ขอเข้าถึงหรือรับสําเนาข้อมูลส่วนบุคคล รวมถึงขอให้โรงพยาบาลสมเด็จพระยุพราชบ้านดุงเปิดเผย'),
                                                  ('2', 'ที่มาของข้อมูลที่ท่านไม่ได้ให้ความยินยอมในการเก็บรวบรวม '),
                                                  ('3', 'ขอแก้ไขข้อมูลส่วนบุคล'),
                                                  ('4', 'ขอให้ลบข้อมูลส่วนบุคคล'),
                                                  ('5', 'ขอคัดค้านการประมวลผลข้อมูลส่วนบุคคล'),
                                                  ('6', 'ขอระงับการประมวลผลข้อมูลส่วนบุคคล ')
                                                  ],
                                       required=False, default='0')


class MDTStatusDocDetail(models.Model):
    _name = 'mdt.status.doc.detail'
    _description = 'Detail document'

    document_id = fields.Many2one(comodel_name='mdm.status.documentt', string='รหัสหัวข้อ', required=False)
    detail_no = fields.Char(string='เลขหน้า', required=False)
    doc_detail = fields.Text(string="เนื้อหาเอกสาร", required=False)
