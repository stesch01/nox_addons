# -*- coding: utf-8 -*-

from odoo import models, fields, api
import xlwt
import cStringIO
import base64
import time

class NoxEventReport(models.TransientModel):
    _name = "nox.event.report"

    name = fields.Char('Name')
    file = fields.Binary('File')
    event_id = fields.Many2one('event.event', 'Event', required=True)

    @api.multi
    def action_generate_report(self):
        for rec in self:
            title_style = xlwt.easyxf('font: height 260, name Calibri Black, colour_index black, bold on; \
                                    align: wrap on, vert centre, horiz centre;\
                                    borders: left thick, right thick, top thick, bottom thick;')
            table_heading_style = xlwt.easyxf('font: height 180, name Calibri Black, colour_index black, bold on; \
                                    align: wrap on, vert centre, horiz centre;\
                                    borders: left thin, right thin, top thin, bottom thin;')

            wb = xlwt.Workbook(encoding='UTF-8')
            ws = wb.add_sheet('Event')

            #row 1 : heading 
            ws.write_merge(0,0,0,3, 'Event - ' + rec.event_id.name, title_style)
            ws.row(0).height = 600

            total_questions = len(rec.event_id.question_ids)
            row = 3

            #set column widths:
            for col in range(0, total_questions + 3):
                ws.col(col).width = 6000

            #write question serial no's
            for col in range(3, total_questions + 3):
                ws.write(row, col, 'Question '+str(col-2), table_heading_style)
                
            #write row heading:
            row += 1
            ws.write(row, 0, 'Name', table_heading_style)
            ws.write(row, 1, 'Phone', table_heading_style)
            ws.write(row, 2, 'Email', table_heading_style)

            col = 3
            #set question ids reference to map the questions answer correctly under each column
            question_ids_list = []
            for question in rec.event_id.question_ids:
                question_ids_list.append(question.id)
                ws.write(row, col, question.title, table_heading_style)
                col += 1
            row += 1

            #write attendee details with question's answers
            attendees = self.env['event.registration'].search_read([('event_id','=',rec.event_id.id)], fields=['name', 'email', 'phone', 'id'])
            for attendee in attendees:
                for col in range(0, 3):
                    if col == 0:
                        ws.write(row, col, attendee['name'])
                    if col == 1:
                        ws.write(row, col, attendee['phone'])
                    if col == 2:
                        ws.write(row, col, attendee['email'])

                col = 3
                for question_id in question_ids_list:
                    attendee_answer = self.env['event.registration.question.answer'].search_read([('event_registration_id', '=', attendee['id']), 
                                            ('question_id','=',question_id)], 
                                            fields=['event_answer'])
                    for answer in attendee_answer:
                        ws.write(row, col, answer['event_answer'])
                        col += 1
                row += 1


            f = cStringIO.StringIO()
            wb.save(f)

            out = base64.encodestring(f.getvalue())
            self.write({'file':out, 'name':('Event_attendees.xls')})

            return {
                'type': 'ir.actions.act_window',
                'res_model': self._name,
                'view_type': 'form',
                'view_mode': 'form',
                'name': 'Events - Report',
                'target': 'new',
                'res_id': int(rec.id),
            }
