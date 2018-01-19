# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################

from odoo.addons.website_event_sale.controllers.main import WebsiteEventSaleController
from odoo import http
from odoo.http import request

from odoo.addons.website.models.website import slug

class WebsiteEventQuestionController(WebsiteEventSaleController):

    @http.route(['/event/<model("event.event"):event>/registration/confirm'], type='http', auth="public", methods=['POST'], website=True)
    def registration_confirm(self, event, **post):
        """redefine function to update Attendee Answers
        """
        Attendees = request.env['event.registration']
        registrations = self._process_registration_details(post)

        order = request.website.sale_get_order(force_create=1)
        attendee_ids = set()

        for registration in registrations:
            ticket = request.env['event.event.ticket'].sudo().browse(int(registration['ticket_id']))
            cart_values = order.with_context(event_ticket_id=ticket.id, fixed_price=True)._cart_update(product_id=ticket.product_id.id, add_qty=1, registration_data=[registration])
            attendee_ids |= set(cart_values.get('attendee_ids', []))

            #Create Attendee Answers:
            for qa in registration:
                question_ref = str(qa).split('questions_ids-')
                if len(question_ref) > 1:
                    question_id = int(question_ref[-1])
                    Question = request.env['event.question'].sudo().browse([question_id])
                    answer = registration[qa]
                    request.env['event.registration.question.answer'].sudo().create({
                            'event_registration_id': list(attendee_ids)[-1],
                            'event_question': Question.title,
                            'event_answer': answer,
                            'question_id': question_id,
                        })

        # free tickets -> order with amount = 0: auto-confirm, no checkout
        if not order.amount_total:
            order.action_confirm()  # tde notsure: email sending ?
            attendees = request.env['event.registration'].browse(list(attendee_ids))
            # clean context and session, then redirect to the confirmation page
            request.website.sale_reset()
            return request.render("website_event.registration_complete", {
                'attendees': attendees,
                'event': event,
            })

        return request.redirect("/shop/checkout")
        
    @http.route(['/event/<model("event.event"):event>/registration/new'], type='json', auth="public", methods=['POST'], website=True)
    def registration_new(self, event, **post):
        """redefine function to call new template
        """
        tickets = self._process_tickets_details(post)
        if not tickets:
            return request.redirect("/event/%s" % slug(event))
        return request.env['ir.ui.view'].render_template("nox_website_event_questions.nox_registration_attendee_details", {'tickets': tickets, 'event': event})
        