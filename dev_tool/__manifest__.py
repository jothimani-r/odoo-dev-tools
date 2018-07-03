# -*- coding: utf-8 -*-
{
    'name': "Developer tools",

    'summary': """Developer tools""",

    'description': """
        
    """,

    'author': "Jothimani R",
    'website': "https://linkedin.com/in/rjothimani/",
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
