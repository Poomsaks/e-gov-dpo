# -*- coding: utf-8 -*-
{
    'name': "E-Gov-DPO",
    'author': "Meditech Insight",
    'description': '',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/main_menu.xml',
        'views/mdm_document_view.xml',
        'views/mdm_position_view.xml',
        'views/custom_res_partner_view.xml',
        'views/mdm_board_iot.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/icon.png'],
}
