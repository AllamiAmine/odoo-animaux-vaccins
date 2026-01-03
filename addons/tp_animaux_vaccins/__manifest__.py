{
    'name': 'Gestion Animaux et Vaccins',
    'version': '1.0',
    'summary': 'Enregistrer les animaux et leurs vaccins',
    'category': 'Education',
    'author': 'Nom Etudiant',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/animal_views.xml',
        'views/vaccin_views.xml',
    ],
    'installable': True,
    'application': True,
}
