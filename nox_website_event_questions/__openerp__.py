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
                website event questions
        """,	
    "demo": [],
    "data": [
	'views/nox_website_event_questions.xml',
    'views/nox_website_event_questions_template.xml',
	'report/nox_website_event_report_menu.xml',
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
