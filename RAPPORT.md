# RAPPORT DE PROJET ERP
## Gestion des Animaux et Vaccins - Module Odoo

---

### Informations du Projet

**Titre**: Système de Gestion des Animaux et Vaccinations  
**Cours**: ERP - Odoo  
**Année Académique**: 2025-2026  
**Étudiant**: [Votre Nom Complet]  
**Numéro d'étudiant**: [Votre Numéro]  
**Date**: Janvier 2026

---

## 1. INTRODUCTION

### 1.1 Contexte du Projet

Ce projet a été développé dans le cadre du cours ERP (Enterprise Resource Planning) en suivant la méthodologie du LAB "Création d'un module Odoo". L'objectif est de créer un module fonctionnel permettant la gestion des animaux et de leurs vaccinations.

### 1.2 Objectifs

Les objectifs principaux de ce projet sont :
- Comprendre l'architecture d'un module Odoo
- Maîtriser la création de modèles de données (ORM)
- Développer des interfaces utilisateur avec XML
- Gérer les relations entre entités (One2many, Many2one)
- Déployer une application avec Docker

### 1.3 Problématique

La gestion manuelle des dossiers de vaccination des animaux est source d'erreurs et de pertes d'information. Ce module vise à centraliser et automatiser la gestion de ces informations critiques pour les vétérinaires et propriétaires d'animaux.

---

## 2. ANALYSE ET CONCEPTION

### 2.1 Analyse des Besoins

#### Besoins Fonctionnels
- **BF1**: Enregistrer les informations des animaux (nom, type, date de naissance)
- **BF2**: Enregistrer les vaccinations avec leurs dates
- **BF3**: Associer plusieurs vaccins à un animal
- **BF4**: Consulter l'historique de vaccination
- **BF5**: Interface intuitive pour la saisie et consultation

#### Besoins Non-Fonctionnels
- **BNF1**: Temps de réponse < 2 secondes
- **BNF2**: Interface en français
- **BNF3**: Sauvegarde automatique des données
- **BNF4**: Compatibilité avec Odoo 17.0

### 2.2 Modélisation des Données

#### Entité Animal
```python
Attributs:
- name (String) : Nom de l'animal [Obligatoire]
- type (Selection) : Type d'animal {Chien, Chat, Vache}
- date_naissance (Date) : Date de naissance
- vaccin_ids (One2many) : Liste des vaccins associés
```

#### Entité Vaccin
```python
Attributs:
- name (String) : Nom du vaccin [Obligatoire]
- date_vaccin (Date) : Date de vaccination
- animal_id (Many2one) : Référence vers l'animal
```

#### Diagramme de Relations
```
┌─────────────────┐         1:N         ┌─────────────────┐
│     Animal      │────────────────────>│     Vaccin      │
├─────────────────┤                     ├─────────────────┤
│ - name          │                     │ - name          │
│ - type          │                     │ - date_vaccin   │
│ - date_naissance│                     │ - animal_id (FK)│
│ - vaccin_ids    │                     └─────────────────┘
└─────────────────┘
```

---

## 3. ARCHITECTURE TECHNIQUE

### 3.1 Stack Technologique

| Composant | Technologie | Version |
|-----------|-------------|---------|
| Framework ERP | Odoo | 17.0 |
| Base de données | PostgreSQL | 15 |
| Langage Backend | Python | 3.10+ |
| Langage Frontend | XML | - |
| Containerisation | Docker | Latest |
| Orchestration | Docker Compose | Latest |

### 3.2 Architecture du Module

```
tp_animaux_vaccins/
│
├── __init__.py                 # Point d'entrée Python
├── __manifest__.py             # Métadonnées et dépendances
│
├── models/                     # Couche Données (ORM)
│   ├── __init__.py
│   ├── animal.py               # Modèle Animal
│   └── vaccin.py               # Modèle Vaccin
│
├── views/                      # Couche Présentation
│   ├── animal_views.xml        # Vues Animal (Tree, Form)
│   └── vaccin_views.xml        # Vues Vaccin + Menus
│
└── security/                   # Couche Sécurité
    └── ir.model.access.csv     # Droits d'accès
```

### 3.3 Architecture Déploiement (Docker)

```
┌─────────────────────────────────────────┐
│         Docker Compose                  │
│  ┌───────────────┐  ┌───────────────┐  │
│  │   odoo_app    │  │   odoo_db     │  │
│  │  (Odoo 17.0)  │  │ (PostgreSQL)  │  │
│  │  Port: 8069   │  │  Port: 5432   │  │
│  └───────┬───────┘  └───────┬───────┘  │
│          │                   │          │
│  ┌───────┴───────────────────┴───────┐ │
│  │      Volumes Persistants           │ │
│  │  - odoo-web-data                   │ │
│  │  - odoo-db-data                    │ │
│  │  - ./addons:/mnt/extra-addons      │ │
│  └────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

---

## 4. IMPLÉMENTATION

### 4.1 Modèle Animal (animal.py)

```python
from odoo import models, fields

class Animal(models.Model):
    _name = 'tp.animal'
    _description = 'Animal'

    # Champs de base
    name = fields.Char(string="Nom", required=True)
    type = fields.Selection([
        ('chien', 'Chien'),
        ('chat', 'Chat'),
        ('vache', 'Vache')
    ], string="Type")
    date_naissance = fields.Date(string="Date de naissance")
    
    # Relation One2many
    vaccin_ids = fields.One2many(
        'tp.vaccin',           # Modèle cible
        'animal_id',           # Champ inverse
        string="Vaccins"
    )
```

**Explication**: 
- `_name`: Identifiant unique du modèle dans Odoo
- `required=True`: Validation obligatoire
- `One2many`: Un animal peut avoir plusieurs vaccins

### 4.2 Modèle Vaccin (vaccin.py)

```python
from odoo import models, fields

class Vaccin(models.Model):
    _name = 'tp.vaccin'
    _description = 'Vaccin'

    name = fields.Char(string="Nom du vaccin", required=True)
    date_vaccin = fields.Date(string="Date du vaccin")
    
    # Relation Many2one
    animal_id = fields.Many2one(
        'tp.animal',           # Modèle parent
        string="Animal",
        ondelete="cascade"     # Suppression en cascade
    )
```

**Explication**:
- `Many2one`: Chaque vaccin appartient à un seul animal
- `ondelete="cascade"`: Si on supprime l'animal, ses vaccins sont supprimés

### 4.3 Vues XML

#### Vue Tree (Liste)
Affiche tous les animaux sous forme de tableau avec colonnes configurables.

#### Vue Form (Formulaire)
Interface détaillée avec :
- Groupe de champs (name, type, date_naissance)
- Notebook avec onglet "Vaccins"
- Tree editable inline pour ajout rapide de vaccins

### 4.4 Sécurité

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_animal,tp.animal,model_tp_animal,,1,1,1,1
access_vaccin,tp.vaccin,model_tp_vaccin,,1,1,1,1
```

Tous les utilisateurs ont accès complet (CRUD).

---

## 5. TESTS ET VALIDATION

### 5.1 Scénarios de Test

#### Test 1: Création d'un Animal
- **Action**: Créer un animal "Rex" de type "Chien"
- **Résultat attendu**: Animal enregistré et visible dans la liste
- **Statut**: ✅ PASS

#### Test 2: Ajout de Vaccins
- **Action**: Ajouter 2 vaccins à "Rex"
- **Résultat attendu**: Vaccins liés et affichés dans l'onglet
- **Statut**: ✅ PASS

#### Test 3: Suppression en Cascade
- **Action**: Supprimer l'animal
- **Résultat attendu**: Vaccins associés supprimés automatiquement
- **Statut**: ✅ PASS

### 5.2 Captures d'Écran

**Note**: Ajoutez vos captures d'écran ici:
- [ ] Page de connexion Odoo
- [ ] Liste des animaux
- [ ] Formulaire de création animal
- [ ] Onglet vaccins avec données
- [ ] Menu principal

---

## 6. GUIDE D'INSTALLATION

### 6.1 Prérequis
- Docker Desktop installé
- 2 GB RAM minimum
- Port 8069 libre

### 6.2 Installation Pas à Pas

```bash
# 1. Cloner le dépôt
git clone [URL_REPOSITORY]
cd odoo-docker

# 2. Lancer Docker
docker compose up -d

# 3. Vérifier les conteneurs
docker ps

# 4. Accéder à Odoo
# http://localhost:8069
```

### 6.3 Configuration Initiale
1. Créer database "odoo"
2. Activer mode développeur
3. Update Apps List
4. Installer "Gestion Animaux et Vaccins"

---

## 7. DIFFICULTÉS RENCONTRÉES

### 7.1 Problèmes Techniques

**Problème 1**: Erreur de syntaxe XML  
**Solution**: Validation avec xmllint et correction des balises

**Problème 2**: Module non visible  
**Solution**: Redémarrage conteneur + Update Apps List

**Problème 3**: Droits d'accès  
**Solution**: Vérification du fichier ir.model.access.csv

---

## 8. AMÉLIORATIONS FUTURES

### Priorité Haute
- Ajout de notifications pour vaccins à renouveler
- Export PDF du carnet de vaccination
- Recherche avancée par type/date

### Priorité Moyenne
- Gestion des propriétaires d'animaux
- Statistiques et graphiques
- Import/Export CSV

### Priorité Basse
- Photos des animaux
- Application mobile
- API REST

---

## 9. CONCLUSION

### 9.1 Compétences Acquises

Au cours de ce projet, j'ai développé les compétences suivantes :
- ✅ Maîtrise de l'architecture MVC dans Odoo
- ✅ Développement en Python (ORM Odoo)
- ✅ Création de vues XML
- ✅ Gestion des relations entre entités
- ✅ Utilisation de Docker pour le déploiement
- ✅ Versionning avec Git/GitHub

### 9.2 Retour d'Expérience

Ce projet m'a permis de comprendre concrètement le fonctionnement d'un ERP et l'importance de la modélisation des données. La méthodologie Odoo facilite grandement le développement grâce à son framework robuste.

### 9.3 Perspective

Les modules Odoo sont modulaires et évolutifs. Ce projet constitue une base solide qui pourrait être étendue pour créer un système complet de gestion vétérinaire.

---

## 10. RÉFÉRENCES

- Documentation Odoo 17: https://www.odoo.com/documentation/17.0/
- LAB Création module Odoo (Cours ERP)
- PostgreSQL Documentation: https://www.postgresql.org/docs/
- Docker Documentation: https://docs.docker.com/

---

## ANNEXES

### Annexe A: Code Complet du Manifest
[Voir fichier __manifest__.py]

### Annexe B: Structure Complète des Fichiers
[Voir README.md]

### Annexe C: Captures d'Écran
[À ajouter]

---

**Fin du Rapport**

---

### Instructions pour Générer le PDF

1. Ouvrir ce fichier dans VS Code
2. Installer l'extension "Markdown PDF"
3. Clic droit → "Markdown PDF: Export (pdf)"
4. Ou utiliser un outil en ligne: https://www.markdowntopdf.com/

**Alternative**:
- Copier le contenu dans Google Docs
- Formater selon vos préférences
- Exporter en PDF
