# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################

{
    "name": "Website event question datatypes",
    "version": "1.0",
    "author": "Linserv AB",
    "category": "Events",
    "website": "www.linserv.se",
    "contributors": [
        'Chandran <chandrantwins@gmail.com>',
        'Riyaj Pathan <rjpathan19@gmail.com>'
        ],
    "license": "",
    "depends": [ 
	   'website_event_questions'
    ],
    'description':"""
                website event questions
        """,	
    "demo": [],
    "data": [
	'views/nox_website_event_questions.xml',
    'views/nox_website_event_questions_template.xml',
    'views/event_views.xml',
	
    'report/website_event_report_menu.xml',
	
    'views/asset.xml',
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [		
	],
    "installable": True,
    "auto_install": False,
}
