{
    'name': "CRM Custom Fields",
    'version': "1.2",
    'author': "Sythil Tech",
    'category': "CRM",
    'summary': "Allows users in the 'Sales / Manager' group to add additional fields to the partner form",
    'license':'LGPL-3',
    'data': [
        'views/res_partner_views.xml',
        'views/ir_model_views.xml',
        'security/ir.model.access.csv',
        'data/crm.custom.fields.widget.csv',
    ],
    'demo': [],
    'depends': ['crm'],
    'images':[
        'static/description/1.jpg',
        'static/description/2.jpg',
        'static/description/3.jpg',
    ],
    'installable': True,
}