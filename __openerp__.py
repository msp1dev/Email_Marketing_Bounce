# -*- coding: utf-8 -*-

{
    'name': 'Email Marketing Bounce',
    'version': '1.0',
    'category': 'Hidden',
    'description': """
Opt out Bounced customers from mailing campaigns to avoid unnecessary load while performing Email Campaigns.
------------------------------------------------------------------------------------------------------------

    """,
    'depends': ['mass_mailing'],
    'data': [
        'bounce_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}