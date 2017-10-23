# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.website_event_questions.controllers.main import WebsiteEvent

import six
import logging
_logger = logging.getLogger(__name__)

class WebsiteEventQuestionController(WebsiteEvent):

    def _process_registration_details(self, details):
        _logger.error("_process_registration_details ............................... ")
        ''' Process data posted from the attendee details form. '''
        registrations = super(WebsiteEventQuestionController, self)._process_registration_details(details)
        for registration in registrations:
            question_ids = []
            for key, value in registration.iteritems():
                _logger.error("KEY: %r", key)
                _logger.error("VALUE: %r", value)
               if key.startswith('questions_ids-') and isinstance(value, six.integer_types):
                    question_ids.append([4, int(value)])
                elif key.startswith('questions_ids-') and isinstance(value, six.string_types):
                    question_ids.append([4, int(key.replace("questions_ids-", ""))])        
            registration['question_ids'] = question_ids

        return registrations

