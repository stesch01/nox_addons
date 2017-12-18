# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################

{
    "name": "Events - Report",
    "version": "1.0",
    "author": "Linserv AB",
    "category": "Reporting",
    "summary": "Events - Report",
    "website": "www.linserv.se",
    "contributors": [
        'Riyaj Pathan <rjpathan19@gmail.com>'
        ],
    "license": "",
    "depends": [ 
        'nox_website_event_questions'
    ],
    'description':"""
##################################################
        Events - Report
##################################################
This module defines functionality to generate xls report for Event.
        """,	
    "demo": [],
    "data": [
        'report/nox_event_report.xml',
    ],
    "installable": True,
    "auto_install": False,
}
