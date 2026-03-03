import os
import time
class Game:
    def __init__(self):
        self.running = True
        self.vie = 10
        self.mot = ""
        self.tab_mot = []
        self.lettre_dites = []

    def crea_mot(self):
        print("Le joueur qui va devinez le mot va devoir fermer les yeux")
        print("L'autre va pendant ce temps entrer un mot")
        return input("Votre mot : ").lower()
    
    def remplissage_mot(self):
        self.tab_mot = ["_" for i in range(len(self.mot))]
    
    def try_lettre(self):
        lettre = input("Entrez une lettre : ").lower()
        return lettre.lower()
    
    def verif_try(self, lettre:str):
        if lettre not in self.lettre_dites:
            self.lettre_dites.append(lettre)
        else:
            print("Lettres deja dites")
            time.sleep(1.5)
            return

        if lettre in self.mot:
            print("BON CHOIX !")
            for test in range(len(self.mot)):
                if self.mot[test] == lettre:
                    self.tab_mot[test] = lettre
        else:
            print("MAUVAIS CHOIX !")
            self.vie -= 1
        time.sleep(1.5)
    
    def affichage(self):
        print(f"Il vous reste : {self.vie} chances")
        print(f"Lettres deja dites : {" ".join(self.lettre_dites)}")
        print(f"Le mot : {(" ".join(self.tab_mot))}")
    
    def verif_vie(self):
        if self.vie <= 0:
            return True
        else:
            return False

    def clear_board(self):
        os.system("clear")

    def run(self):

        while self.running :
            print("Jeu se jouant a 2 joueur")
            print("L'un va choisir un mot et l'autre va essayer de le trouver")
            self.mot = self.crea_mot()
            self.remplissage_mot()
            print("Maintenant que le mot est choisit, le premier joueur va essayer de le deviner")
            while not self.verif_vie() and "_" in self.tab_mot:
                self.clear_board()
                print("........................................................................")
                self.affichage()
                lettre = self.try_lettre()
                self.verif_try(lettre[0])
                print("........................................................................")

            self.clear_board()
            print("........................................................................")
            if self.vie <= 0:
                print("Tu as perdu...")
                print(f"Le mot etait : {self.mot}")
            else:
                print("WIN !!!")
            
            if input("Recommencer ? <O>ui ou <N>on : ").upper() == "N":
                print("........................................................................")
                self.running = False

if __name__ == "__main__":
    Game().run()