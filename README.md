
# Pylist V1

**Auteur** : Axel INGRAO  
**Licence** : GPL

## Description

Pylist V1 est une application de gestion de tâches simple en ligne de commande. Elle permet à l'utilisateur d'ajouter, de visualiser, de supprimer des tâches, et d'enregistrer ces tâches dans un fichier de configuration. Ce programme lit et écrit dans un fichier de configuration `config.cfg` pour stocker les tâches entre les sessions.

## Fonctionnalités

- **Ajouter une tâche** : Permet à l'utilisateur d'ajouter une tâche à la liste.
- **Voir les tâches** : Affiche toutes les tâches sauvegardées.
- **Supprimer une tâche** : Permet de supprimer une tâche de la liste en fonction de son index.
- **Quitter l'application** : Sauvegarde les tâches dans le fichier `config.cfg` et quitte l'application.

## Installation

1. Clonez ou téléchargez le fichier `pylist.py`.
2. Assurez-vous que Python est installé sur votre machine (version 3.x recommandée).
3. Lancez le programme via la ligne de commande avec :

   ```bash
   python pylist.py
   ```

Le programme gère automatiquement la création du fichier `config.cfg` si celui-ci n'existe pas déjà.

## Utilisation

Lorsque vous lancez l'application, l'interface de ligne de commande vous présente plusieurs options :

1. **Ajouter une tâche** : Vous pouvez entrer une nouvelle tâche.
2. **Voir les tâches** : Affiche la liste de toutes les tâches sauvegardées.
3. **Supprimer une tâche** : Vous pouvez supprimer une tâche en spécifiant son index.
4. **Quitter** : Quitte le programme après avoir sauvegardé les modifications dans le fichier `config.cfg`.

### Exemple d'utilisation

```
Bienvenue dans Pylist
Entrez ce que vous voulez faire :
1 = Ajoutez une tâche
2 = Voir les tâches
3 = supprimer une tâche
4 = Sortie

Entrez votre choix : 1
entrez le nom de la tâche : Acheter des légumes

Entrez votre choix : 2
0 Acheter des légumes

Entrez votre choix : 3
Entrez l'index de la tâche à supprimer : 0

Entrez votre choix : 4
```

## Structure du Code

Le programme est structuré en plusieurs modules/fonctions :

1. **Module_affichage()** : Affiche le menu principal et les options disponibles.
2. **Module_creation()** : Crée le fichier `config.cfg` s'il n'existe pas.
3. **Module_fichier(Liste_Saved)** : Sauvegarde les tâches dans le fichier `config.cfg`.
4. **Module_lecture()** : Lit les tâches sauvegardées à partir du fichier `config.cfg`.

### Dépendances

Le programme utilise uniquement la bibliothèque standard Python (`os`), il n'y a donc aucune dépendance externe.

## Licence

Ce programme est distribué sous la **GPL** (General Public License).
