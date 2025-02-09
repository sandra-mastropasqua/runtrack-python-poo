import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts!")
    
    def est_vivant(self):
        return self.vie > 0
    
    def afficher_vie(self):
        print(f"{self.nom} : {self.vie} points de vie restants.")

class Jeu:
    def __init__(self):
        self.niveau = None
    
    def choisirNiveau(self):
        niveau = input("Choisissez un niveau de difficulté (facile, moyen, difficile) : ").lower()
        if niveau not in ["facile", "moyen", "difficile"]:
            print("Niveau invalide, mode moyen sélectionné par défaut.")
            self.niveau = "moyen"
        else:
            self.niveau = niveau
    
    def lancerJeu(self):
        if self.niveau == "facile":
            vie_joueur, vie_ennemi = 100, 50
        elif self.niveau == "moyen":
            vie_joueur, vie_ennemi = 100, 100
        else:
            vie_joueur, vie_ennemi = 100, 150

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)
        
        print("Le combat commence!")
        
        while joueur.est_vivant() and ennemi.est_vivant():
            joueur.attaquer(ennemi)
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)
            
            joueur.afficher_vie()
            ennemi.afficher_vie()
            print("-------------------------")
        
        self.afficherGagnant(joueur, ennemi)
    
    def afficherGagnant(self, joueur, ennemi):
        if joueur.est_vivant():
            print("Bravo, vous avez gagné!")
        else:
            print("Dommage, vous avez perdu!")


jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()