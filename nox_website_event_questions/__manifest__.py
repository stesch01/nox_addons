# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################

{
    "name": "Website event question datatypes",
    "version": "11.0",
    "author": "Linserv AB",
    "category": "Events",
    "summary": "Website event question datatypes",
    "website": "www.linserv.se",
    "contributors": [
        'Chandran <chandrantwins@gmail.com>',
        'Riyaj Pathan <rjpathan19@gmail.com>'
        ],
    "license": "",
    "depends": [ 
        'website_event_questions',
        'website_event_sale'
    ],
    "external_dependencies": {'python': ['xlwt']},
    
    'description':"""
##################################################
    Website event question datatypes
##################################################
This modules adds different data types to define Event Questions.    
    * Data Types :
        * Text
        * Longtext
        * Email
        * Dropdown
        * Checkbox
        * Radio
        * Number

It also defines functionality to generate xls report for Event.
        """,	
    "demo": [],
    "data": [
	'views/nox_website_event_questions.xml',
    'views/nox_website_event_questions_template.xml',
    'views/event_views.xml',
	
    'report/website_event_report_menu.xml',
	
    'views/asset.xml',

    'security/ir.model.access.csv',
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [		
	],
    "installable": True,
    "auto_install": False,
}
