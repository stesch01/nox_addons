# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################

from odoo import models, fields, api, _

class eventquestion_datatype(models.Model):
    _inherit = 'event.question'

    data_type = fields.Selection([('text', 'Text'), 
    							('longtext', 'Longtext'), 
    							('email', 'Email'), 
    							('dropdown', 'Dropdown'), 
    							('checkbox', 'Checkbox'),
    							('radio', 'Radio'),
    							('number', 'Number')], string='Datatypes')
    note = fields.Text('Comment')