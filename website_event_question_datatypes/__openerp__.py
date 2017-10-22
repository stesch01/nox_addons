# coding: utf-8
###########################################################################
#    Module Written using Odoo, Open Source Management Solution
###############Credits######################################################
#    Coded by: Chandran Nepolean <chandrantwins@gmail.com>,
#############################################################################
{
    "name": "Website event question datatypes",
    "version": "1.0",
    "author": "Chandran",
    "category": "Events",
    "website": "",
    "license": "",
    "depends": [ 
	'website_event_questions'
    ],
    'description':"""
                website event question datatypes
        """,	
    "demo": [],
    "data": [
	'views/website_event_question_datatypes_backend.xml',
    'views/website_event_question_datatypes_template.xml',
	'report/website_event_report_menu.xml',
	'views/asset.xml'
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [		
	],
    "installable": True,
    "auto_install": True,
}
