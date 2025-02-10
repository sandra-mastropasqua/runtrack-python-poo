import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def points(self):
        if self.valeur in ["Valet", "Dame", "Roi"]:
            return 10
        elif self.valeur == "As":
            return 11  
        else:
            return int(self.valeur)
    
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)
    
    def piocher(self):
        return self.paquet.pop() if self.paquet else None

def calculer_score(main):
    score = sum(carte.points() for carte in main)
    as_count = sum(1 for carte in main if carte.valeur == "As")
    
    while score > 21 and as_count:
        score -= 10  
        as_count -= 1
    
    return score

def afficher_main(joueur, main):
    print(f"Main de {joueur}: {', '.join(str(carte) for carte in main)} (Score: {calculer_score(main)})")

def jouer_blackjack():
    jeu = Jeu()
    joueur_main = [jeu.piocher(), jeu.piocher()]
    croupier_main = [jeu.piocher(), jeu.piocher()]
    
    afficher_main("Joueur", joueur_main)
    
    while calculer_score(joueur_main) < 21:
        action = input("Voulez-vous prendre une carte ? (oui/non): ").lower()
        if action == "oui":
            joueur_main.append(jeu.piocher())
            afficher_main("Joueur", joueur_main)
        else:
            break
    
    if calculer_score(joueur_main) > 21:
        print("Vous avez dépassé 21 ! Vous perdez.")
        return
    
    print("Tour du croupier...")
    while calculer_score(croupier_main) < 17:
        croupier_main.append(jeu.piocher())
    afficher_main("Croupier", croupier_main)
    
    joueur_score = calculer_score(joueur_main)
    croupier_score = calculer_score(croupier_main)
    
    if croupier_score > 21 or joueur_score > croupier_score:
        print("Félicitations ! Vous avez gagné !")
    elif joueur_score < croupier_score:
        print("Le croupier gagne. Vous avez perdu.")
    else:
        print("Égalité !")

if __name__ == "__main__":
    jouer_blackjack()
