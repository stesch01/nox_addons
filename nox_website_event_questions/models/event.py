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

    @api.model
    def default_get(self, fields):
        res = super(eventquestion_datatype, self).default_get(fields)

        #set default value checked
        res.update({'is_individual': True})
        return res

class EventRegistration(models.Model):
    _inherit = "event.registration"

    @api.multi
    def compute_total_answers(self):
        for attendee in self:
            attendee.total_answers = len(attendee.attendee_answer_ids)

    attendee_answer_ids = fields.One2many('event.registration.question.answer', 'event_registration_id', 'Answers')
    total_answers = fields.Integer(compute='compute_total_answers', string='Answers', store=False)

    @api.multi
    def action_open_answers(self):
        for attendee in self:
            attendee_answers = []
            temp = [attendee_answers.append(at.id) for at in attendee.attendee_answer_ids] 
            if attendee_answers:
                action = attendee.env.ref('nox_website_event_questions.action_event_registration_question_answers').read()[0]
                action['domain'] = [['id', 'in', attendee_answers]]
                return action
            return True

class EventRegistrationQAnswer(models.Model):
    _name = "event.registration.question.answer"
    _description = "Event Attendee - Question's Answers"

    @api.depends('event_registration_id.state')
    def set_attendee_state(self):
        for answer in self:
            answer.state = answer.event_registration_id.state

    event_registration_id = fields.Many2one('event.registration', 'Attendee')
    state = fields.Selection(compute="set_attendee_state", selection=[('draft', 'Unconfirmed'), 
                                ('cancel', 'Cancelled'),
                                ('open', 'Confirmed'), 
                                ('done', 'Attended')], string='Status', store=True)
    event_id = fields.Many2one(related='event_registration_id.event_id', string='Event', store=True)
    event_question = fields.Char('Question')
    event_answer = fields.Char('Answer')
