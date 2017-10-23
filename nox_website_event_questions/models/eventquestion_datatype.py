# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################

from odoo import models, fields, api, _

class question_datatype(models.Model):
    _name = 'question.datatype'
    _order = 'id'

    name = fields.Char('Name', required=True, translate=True)

class eventquestion_datatype(models.Model):
    _inherit = 'event.question'

    data_type_id = fields.Many2one('question.datatype', string='Datatypes')     
