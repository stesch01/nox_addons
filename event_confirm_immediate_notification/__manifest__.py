# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################

{
    "name": "Auto Send Event confirmation email",
    "version": "1.0",
    "author": "Linserv AB",
    "category": "Messaging",
    "summary": "Auto Send Event confirmation email",
    "website": "www.linserv.se",
    "contributors": [
        'Riyaj Pathan <rjpathan19@gmail.com>'
        ],
    "license": "",
    "depends": [ 
        'event'
    ],
    'description':"""
##################################################
        Auto Send Event confirmation email
##################################################
This module triggers immediate email notification send on new Attendee registration.
        """,	
    "demo": [],
    "data": [
    ],
    "installable": True,
    "auto_install": False,
}
