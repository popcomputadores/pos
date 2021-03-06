# Copyright 2004-2010 OpenERP SA
# Copyright 2017 RGB Consulting S.L. (https://www.rgbconsulting.com)
# Copyright 2018 Lambda IS DOOEL <https://www.lambda-is.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Loyalty Program',
    'version': '11.0.1.0.0',
    'category': 'Point of Sale',
    'license': 'AGPL-3',
    'author': "OpenERP SA, "
              "RGB Consulting SL, "
              "Lambda IS, "
              "Odoo Community Association (OCA)",
    'website': "https://odoo-community.org/",
    'depends': ['point_of_sale'],
    'demo': [
        'demo/templates.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/loyalty_program_view.xml',
        'views/loyalty_reward_view.xml',
        'views/loyalty_rule_view.xml',
        'views/pos_config_view.xml',
        'views/pos_order_view.xml',
        'views/res_partner_view.xml',
    ],

    'qweb': [
        'static/src/xml/pos.xml',
    ],

    'installable': True,
}
