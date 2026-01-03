# 🐾 Gestion Animaux et Vaccins - Module Odoo

## 📋 Description du Projet

Module Odoo développé dans le cadre du cours ERP permettant la gestion complète des animaux et de leurs vaccinations. Ce système permet de :
- Enregistrer et gérer des animaux (chiens, chats, vaches)
- Suivre l'historique complet des vaccinations
- Associer plusieurs vaccins à chaque animal
- Consulter facilement les informations de vaccination

## 👨‍🎓 Informations Académiques

- **Cours**: ERP - Odoo
- **Projet**: LAB Création module Odoo
- **Année**: 2025-2026
- **Auteur**: [AMINE ALLAMI]

## 🎯 Fonctionnalités

### Gestion des Animaux
- ✅ Enregistrement des informations de base (nom, type, date de naissance)
- ✅ Types d'animaux supportés : Chien, Chat, Vache
- ✅ Vue liste et formulaire détaillé
- ✅ Relation One2many avec les vaccins

### Gestion des Vaccins
- ✅ Enregistrement des vaccinations
- ✅ Suivi des dates de vaccination
- ✅ Association automatique à l'animal
- ✅ Edition directe depuis le formulaire animal

## 🛠️ Technologies Utilisées

- **Odoo**: Version 17.0
- **PostgreSQL**: Version 15
- **Docker**: Containerisation
- **Python**: Backend (models)
- **XML**: Frontend (views)

## 📦 Installation

### Prérequis
- Docker et Docker Compose installés
- 2 GB de RAM minimum
- Port 8069 disponible

### Étapes d'Installation

1. **Cloner le dépôt**
```bash
git clone [VOTRE_URL_GIT]
cd odoo-docker
```

2. **Lancer Docker**
```bash
docker compose up -d
```

3. **Attendre le démarrage** (30-60 secondes)
```bash
docker logs -f odoo_app
```

4. **Accéder à Odoo**
- URL: http://localhost:8069
- Créer une nouvelle base de données
  - Master Password: `admin`
  - Database Name: `odoo`
  - Email: `admin@example.com`
  - Password: `admin`

5. **Activer le mode développeur**
- Settings → Developer Tools → Activate the developer mode

6. **Installer le module**
- Apps → Update Apps List
- Rechercher "Gestion Animaux et Vaccins"
- Cliquer sur Install

## 📖 Utilisation

### Créer un Animal

1. Menu → **Animaux** → **Créer**
2. Remplir les informations:
   - Nom: Ex. "Rex"
   - Type: Choisir parmi Chien/Chat/Vache
   - Date de naissance: Sélectionner la date
3. Cliquer sur **Enregistrer**

### Ajouter des Vaccins

1. Dans le formulaire de l'animal
2. Onglet **Vaccins**
3. Cliquer sur **Ajouter une ligne**
4. Remplir:
   - Nom du vaccin: Ex. "Rage"
   - Date du vaccin: Sélectionner la date
5. Enregistrer

### Consulter les Vaccins

- Menu → **Vaccins** → Vue de tous les vaccins enregistrés

## 📂 Structure du Projet

```
odoo-docker/
├── docker-compose.yml          # Configuration Docker
├── README.md                   # Documentation
├── rapport.pdf                 # Rapport du projet
└── addons/
    └── tp_animaux_vaccins/     # Module Odoo
        ├── __init__.py
        ├── __manifest__.py     # Métadonnées du module
        ├── models/             # Modèles de données
        │   ├── __init__.py
        │   ├── animal.py       # Modèle Animal
        │   └── vaccin.py       # Modèle Vaccin
        ├── views/              # Interfaces utilisateur
        │   ├── animal_views.xml
        │   └── vaccin_views.xml
        └── security/           # Droits d'accès
            └── ir.model.access.csv
```

## 🗄️ Modèles de Données

### Modèle Animal (`tp.animal`)
| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom de l'animal (obligatoire) |
| type | Selection | Type: Chien/Chat/Vache |
| date_naissance | Date | Date de naissance |
| vaccin_ids | One2many | Liste des vaccins |

### Modèle Vaccin (`tp.vaccin`)
| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom du vaccin (obligatoire) |
| date_vaccin | Date | Date de vaccination |
| animal_id | Many2one | Animal associé |

## 🔐 Sécurité

Les droits d'accès sont configurés dans `ir.model.access.csv`:
- Lecture, écriture, création et suppression activés pour tous les utilisateurs
- Possibilité de restreindre par groupes selon les besoins

## 🚀 Commandes Utiles

```bash
# Voir les logs en temps réel
docker logs -f odoo_app

# Redémarrer Odoo
docker compose restart odoo_app

# Arrêter tous les services
docker compose down

# Relancer les services
docker compose up -d

# Accéder au shell du conteneur
docker exec -it odoo_app bash
```

## 🐛 Dépannage

### Le module n'apparaît pas
1. Vérifier que les fichiers sont dans `/mnt/extra-addons`
2. Activer le mode développeur
3. Update Apps List

### Erreur de permissions
```bash
docker compose down
docker compose up -d
```

### Port 8069 déjà utilisé
Modifier le port dans `docker-compose.yml`:
```yaml
ports:
  - "8070:8069"  # Utiliser 8070 au lieu de 8069
```

## 📝 Améliorations Futures

- [ ] Ajout de rappels automatiques pour les vaccins
- [ ] Statistiques et rapports
- [ ] Export PDF des carnets de vaccination
- [ ] Gestion des propriétaires d'animaux
- [ ] Photos des animaux
- [ ] Alertes pour vaccins expirés

## 📄 Licence

Projet académique - ERP Course

## 📧 Contact

[Votre Email]

---

**Note**: Ce projet a été développé dans le cadre du cours ERP suivant la méthodologie du LAB Création module Odoo.
