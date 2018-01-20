# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################

from odoo import models, api

class MailMail(models.Model):
    _inherit = "mail.mail"

    @api.model
    def create(self, vals):
    	"""Immediate send Event Confirmation email on mail creation
    	"""
    	res = super(MailMail, self).create(vals)
    	context = self.env.context or {}
    	if context.get('event_confirmation_immediate_send', False):
    		res.send()
    	return res
    	