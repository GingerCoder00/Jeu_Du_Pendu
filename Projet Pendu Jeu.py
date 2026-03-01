# Créé par leguludec, le 06/09/2025 en Python 3.7
from random import randint
import os

jeu = 1
win1 = 0
win2 = 0

def crea_mot():
    print("Le joueur qui va devinez le mot va devoir fermer les yeux")
    print("L'autre va pendant ce temps entrer un mot")
    mot = input("Votre mot : ")
    print("Mot recu !!!")
    return mot.lower()
    
def try_lettre(mot):
    print("...................................................")
    lettre = input("Entrez une lettre : ").lower()
    return lettre.lower()

def affichage(mot):
    print("...................................................")
    tab_mot = ["_" for i in range(len(mot))]
    return tab_mot

def verif_vie(vie,mot):
    if vie <= 0:
        print("Vous avez perdu ...")
        print(f"Le mot etait : {mot}")
        return 1
    else:
        return 0
    
def verif_gain(gain,mot):
    if gain >= len(mot):
        print("SUPER VOUS AVEZ GAGNE !!!")
        print(f"Le mot etait bien : {mot.upper()} !")
        return 1
    else:
        return 0

def clear_board():
    c1= os.system("cls") # Windows
    c1 = os.system("clear") # De type Unix

while jeu == 1:
    gain = 0
    vie = 10
    lettre_fausse = []
    print("Jeu se jouant a 2 joueur")
    print("L'un va choisir un mot et l'autre va essayer de le trouver")
    mot = crea_mot()
    clear_board()
    print("Maintenant que le mot est choisit, le premier joueur va essayer de le deviner")
    tab_mot = affichage(mot)
    while win1 == 0 and win2 == 0:
        print(f"Il vous reste : {vie} chances")
        print(f"Lettres deja dites : {" ".join(lettre_fausse)}")
        print(f"Le mot : {(" ".join(tab_mot))}")
        lettre = try_lettre(mot)
        if lettre in mot:
            print("BON CHOIX !")
            for j in range(len(mot)):
                if mot[j] == lettre:
                    if lettre not in tab_mot:
                        gain += mot.count(lettre)
                    tab_mot[j] = lettre
                    if lettre not in lettre_fausse:
                        lettre_fausse.append(lettre)
        else:
            print("MAUVAIS CHOIX !")
            if lettre not in lettre_fausse:
                lettre_fausse.append(lettre)
                vie -= 1
        win1 = verif_vie(vie,mot)
        win2 = verif_gain(gain,mot)
    choix2 = int(input("Voulez vous rejouer ? (Tapez 1 pour oui ou 2 pour non) : "))
    if choix2 == 2:
        jeu = 0    