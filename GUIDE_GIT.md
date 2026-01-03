# 📤 Guide de Déploiement sur GitHub/GitLab

## ✅ Ce qui a été fait automatiquement:

- ✅ Git initialisé
- ✅ Tous les fichiers ajoutés
- ✅ Premier commit créé
- ✅ .gitignore configuré

---

## 🚀 OPTION 1: GitHub (Recommandé)

### Étape 1: Créer le Repository sur GitHub

1. **Aller sur GitHub**: https://github.com
2. **Se connecter** ou créer un compte
3. Cliquer sur le **+** en haut à droite → **New repository**

4. **Remplir les informations**:
   ```
   Repository name: odoo-animaux-vaccins
   Description: Module Odoo - Gestion des Animaux et Vaccinations (Projet ERP)
   Visibilité: ☑️ Public
   
   ⚠️ NE PAS cocher:
   - Add README
   - Add .gitignore
   - Choose a license
   ```

5. Cliquer **Create repository**

### Étape 2: Pusher le Code

Copier et exécuter ces commandes dans votre PowerShell:

```powershell
# Remplacer VOTRE_USERNAME par votre nom d'utilisateur GitHub
git remote add origin https://github.com/VOTRE_USERNAME/odoo-animaux-vaccins.git

# Pusher le code
git branch -M main
git push -u origin main
```

**Exemple**:
```powershell
git remote add origin https://github.com/aminallami/odoo-animaux-vaccins.git
git branch -M main
git push -u origin main
```

### Étape 3: Vérifier

1. Rafraîchir la page GitHub
2. Vous devriez voir tous vos fichiers ✅
3. Le README.md s'affiche automatiquement

### Étape 4: Convertir RAPPORT.md en PDF

**Option A - Avec VS Code**:
1. Installer l'extension "Markdown PDF"
2. Ouvrir `RAPPORT.md`
3. `Ctrl+Shift+P` → "Markdown PDF: Export (pdf)"
4. Le fichier `rapport.pdf` sera créé

**Option B - En ligne**:
1. Aller sur: https://www.markdowntopdf.com/
2. Copier tout le contenu de `RAPPORT.md`
3. Coller et télécharger le PDF

**Option C - Google Docs**:
1. Copier le contenu de `RAPPORT.md`
2. Coller dans Google Docs
3. Fichier → Télécharger → PDF

### Étape 5: Ajouter le PDF au Repository

```powershell
# Après avoir créé rapport.pdf
git add rapport.pdf
git commit -m "Ajout du rapport PDF"
git push
```

### Étape 6: Obtenir le Lien pour Classroom

Votre lien Git sera:
```
https://github.com/VOTRE_USERNAME/odoo-animaux-vaccins
```

**C'est ce lien que vous déposerez dans Google Classroom** ✅

---

## 🦊 OPTION 2: GitLab

### Étape 1: Créer le Repository sur GitLab

1. **Aller sur GitLab**: https://gitlab.com
2. **Se connecter** ou créer un compte
3. Cliquer **New project** → **Create blank project**

4. **Remplir**:
   ```
   Project name: odoo-animaux-vaccins
   Visibility: Public
   
   ⚠️ Décocher: Initialize repository with a README
   ```

5. **Create project**

### Étape 2: Pusher le Code

```powershell
# Remplacer VOTRE_USERNAME par votre nom GitLab
git remote add origin https://gitlab.com/VOTRE_USERNAME/odoo-animaux-vaccins.git

git branch -M main
git push -u origin main
```

### Étape 3: Lien pour Classroom

```
https://gitlab.com/VOTRE_USERNAME/odoo-animaux-vaccins
```

---

## 📋 Checklist Finale

Avant de déposer le lien, vérifier:

- [ ] Repository est **PUBLIC** ou accessible
- [ ] README.md présent et complet
- [ ] rapport.pdf présent (converti depuis RAPPORT.md)
- [ ] Dossier `addons/tp_animaux_vaccins/` avec tous les fichiers
- [ ] `docker-compose.yml` présent
- [ ] `.gitignore` configuré
- [ ] Aucun fichier sensible (mots de passe, .env)

---

## 🔧 Commandes Git Utiles

```powershell
# Voir le statut
git status

# Voir l'historique
git log --oneline

# Ajouter des modifications
git add .
git commit -m "Description des changements"
git push

# Vérifier le remote
git remote -v
```

---

## ❌ Problèmes Courants

### Erreur: "Authentication failed"

**Solution**: Utiliser un Personal Access Token au lieu du mot de passe

**GitHub**:
1. Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Cocher `repo`
4. Copier le token
5. Utiliser ce token comme mot de passe lors du push

### Erreur: "Repository not found"

**Solution**: Vérifier l'URL et que le repo existe
```powershell
git remote -v
git remote set-url origin https://github.com/USERNAME_CORRECT/repo-correct.git
```

### Fichiers trop volumineux

Les PDFs dans le dossier sont OK, mais éviter de pusher:
- Images très lourdes (> 100MB)
- Fichiers compilés
- Bases de données

---

## 📧 Contenu du Message pour Classroom

```
Lien Git: https://github.com/VOTRE_USERNAME/odoo-animaux-vaccins

Le repository contient:
✅ Code source du module Odoo (addons/tp_animaux_vaccins/)
✅ Fichier README.md avec documentation complète
✅ Fichier rapport.pdf
✅ docker-compose.yml pour déploiement
✅ Instructions d'installation

Le module implémente la gestion des animaux et de leurs vaccinations
avec relations One2many/Many2one selon la méthodologie du LAB ERP.
```

---

## 🎯 Prochaines Étapes

1. ✅ Créer le repository GitHub/GitLab
2. ✅ Pusher le code
3. ✅ Convertir RAPPORT.md → rapport.pdf
4. ✅ Pusher le PDF
5. ✅ Vérifier que tout est visible
6. ✅ Copier le lien
7. ✅ Déposer dans Google Classroom

---

**Bonne chance! 🚀**
