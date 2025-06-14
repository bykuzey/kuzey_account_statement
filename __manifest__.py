{
    'name': 'Kuzey Cari Ekstre',
    'version': '1.0',
    'summary': 'Cari Hesap Ekstre Raporu',
    'category': 'Accounting',
    'author': 'Kuzey ERP',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'models/model_access.xml',
        'wizard/wizard_views.xml',
        'views/menu.xml',
        'report/statement_report.xml'
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True
}
