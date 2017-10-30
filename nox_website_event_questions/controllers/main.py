# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################

from odoo.addons.website_event_questions.controllers.main import WebsiteEvent
from odoo import http
from odoo.http import request

class WebsiteEventQuestionController(WebsiteEvent):

    @http.route(['/event/<model("event.event"):event>/registration/confirm'], type='http', auth="public", methods=['POST'], website=True)
    def registration_confirm(self, event, **post):
        """redefine function to update Attendee Answers
        """
        Attendees = request.env['event.registration']
        registrations = super(WebsiteEventQuestionController, self)._process_registration_details(post)

        for registration in registrations:
            registration['event_id'] = event
            attendee_id = Attendees.sudo().create(
                Attendees._prepare_attendee_values(registration))
            Attendees += attendee_id
            #create attendee answers:
            for qa in registration:
                question_ref = str(qa).split('questions_ids-')
                if len(question_ref) > 1:
                    question_id = int(question_ref[-1])
                    Question = request.env['event.question'].sudo().browse([question_id])
                    answer = registration[qa]
                    request.env['event.registration.question.answer'].sudo().create({
                            'event_registration_id': attendee_id.id,
                            'event_question': Question.title,
                            'event_answer': answer
                        })

        return request.render("website_event.registration_complete", {
            'attendees': Attendees,
            'event': event,
        })