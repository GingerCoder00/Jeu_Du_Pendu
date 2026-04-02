# Pendu — Jeu à 2 joueurs

Un jeu du **Pendu en mode local 2 joueurs**, entièrement en Python.  
Un joueur choisit secrètement un mot, l'autre tente de le deviner  
lettre par lettre avant d'épuiser ses **10 chances**.

---

## Comment jouer

1. **Joueur 1** entre un mot secret (l'autre ferme les yeux 👀)
2. L'écran est effacé automatiquement pour garder le secret
3. **Joueur 2** propose des lettres une par une
4. Chaque mauvaise lettre coûte une vie — il en a **10 au total**
5. Le mot est affiché progressivement au fur et à mesure des bonnes réponses
6. À la fin, les joueurs peuvent choisir de **rejouer**

---

## Lancer le jeu

**Prérequis :** Python 3.7+  — aucune dépendance externe
```bash
git clone https://github.com/leguludec/pendu.git
cd pendu
python pendu.py
```

---

## Exemple de partie
```
Jeu se jouant a 2 joueurs
L'un va choisir un mot et l'autre va essayer de le trouver
Votre mot : python
Mot recu !!!

[écran effacé]

Maintenant que le mot est choisit, le premier joueur va essayer de le deviner
...................................................
Il vous reste : 10 chances
Lettres deja dites : 
Le mot : _ _ _ _ _ _
Entrez une lettre : p
BON CHOIX !
...
SUPER VOUS AVEZ GAGNE !!!
Le mot etait bien : PYTHON !
```

---

## 🗂️ Structure du projet
```
pendu/
│
├── pendu.py    # Script principal
├── LICENSE     # LICENSE du projet
└── README.md
```

---

## Fonctionnalités

- Saisie sécurisée du mot secret avec effacement automatique de l'écran (Windows & Unix)
- Suivi des lettres déjà proposées (bonnes et mauvaises)
- Affichage progressif du mot avec les lettres trouvées
- Compteur de vies et détection automatique de victoire/défaite
- Option de rejouer en fin de partie

---

## Pistes d'amélioration

- Ajouter un mode solo avec une liste de mots aléatoires
- Afficher un vrai dessin du pendu étape par étape
- Gérer les accents et les caractères spéciaux
- Ajouter un score cumulé sur plusieurs manches

---

## Auteur

Créé par **LE GULUDEC ARTHUR** — Septembre 2025

---

## Licence

MIT — libre d'utilisation, de modification et de partage.
