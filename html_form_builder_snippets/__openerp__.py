{
    'name': "HTML Form Builder - Website Snippets",
    'version': "1.8.13",
    'author': "Sythil",
    'category': "Tools",
    'summary': "Generates bootstrap forms and add extra fields by dragging snippets",
    'description': "Generates bootstrap forms and add extra fields by dragging snippets",
    'license':'LGPL-3',
    'data': [
        'views/snippets.xml',
        'views/website_templates.xml',
        'data/html.form.snippet.action.csv',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'images':[
        'static/description/3.jpg',
        'static/description/1.jpg',
        'static/description/2.jpg',
    ],
    'depends': ['website','html_form_builder'],
    'installable': True,
}