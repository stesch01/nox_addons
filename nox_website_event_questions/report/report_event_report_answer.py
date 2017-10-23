# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools

class ReportEventAnswerReport(models.Model):
    _name = "event.report.answer.report"
    _auto = False
    
    id  =  fields.Char(string='id')
    create_date = fields.Char(string='create_date')
    attendeename = fields.Char(string='attendeename')
    eventname = fields.Char(string='Event')
    answername = fields.Char(string='Answer')   
    questiontitle = fields.Char(string='Question')
    eventtypename = fields.Char(string='EventType')
    
    @api.model_cr
    def init(self):
        """ Event Question main report """
        tools.drop_view_if_exists(self._cr, 'event_report_answer_report')
        self._cr.execute(""" CREATE VIEW event_report_answer_report AS (
            SELECT
                att_answer.id as id,
                answer.create_date as create_date,
                reg.name as attendeename,
                answer.name as answername,
                question.title as questiontitle,
                eventtype.name as eventtypename,
                event.name || '(' || to_char(date_begin,'YYYY/MM/DD') ||'- '||to_char(date_end,'YYYY/MM/DD')||')' as eventname
            FROM
                event_registration_answer as att_answer
            LEFT JOIN
                event_answer as answer ON answer.id = att_answer.event_answer_id
            LEFT JOIN
                event_question as question ON question.id = answer.question_id
            left join 
                event_registration as reg on reg.id=att_answer.event_registration_id    
            Left join 
                event_event as event on event.id=reg.event_id 
            LEFT JOIN
                event_type as eventtype on eventtype.id=event.event_type_id
        )""")
