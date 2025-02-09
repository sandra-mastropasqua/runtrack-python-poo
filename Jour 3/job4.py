class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
    
    def marquerUnBut(self):
        self.buts += 1
    
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
    
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
    
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
    
    def afficherStatistiques(self):
        return (f"{self.nom} (#{self.numero}, {self.position}) - Buts: {self.buts}, "
                f"Passes décisives: {self.passes_decisives}, Cartons jaunes: {self.cartons_jaunes}, "
                f"Cartons rouges: {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())
    
    def mettreAJourStatistiquesJoueur(self, nom, action):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton rouge":
                    joueur.recevoirUnCartonRouge()


equipe1 = Equipe("OM")
equipe2 = Equipe("PSG")


joueur1 = Joueur("Antoine", 10, "Attaquant")
joueur2 = Joueur("Sandra", 8, "Milieu")
joueur3 = Joueur("Emma", 5, "Défenseur")

joueur4 = Joueur("Nabil", 7, "Attaquant")
joueur5 = Joueur("Eric", 6, "Milieu")
joueur6 = Joueur("Bruno", 4, "Défenseur")


equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)

equipe2.ajouterJoueur(joueur4)
equipe2.ajouterJoueur(joueur5)
equipe2.ajouterJoueur(joueur6)


equipe1.mettreAJourStatistiquesJoueur("Nabil", "but")
equipe2.mettreAJourStatistiquesJoueur("Antoine", "passe")
equipe1.mettreAJourStatistiquesJoueur("Emma", "carton jaune")
equipe2.mettreAJourStatistiquesJoueur("Sandra", "carton rouge")


print("Statistiques de l'OMG:")
equipe1.afficherStatistiquesJoueurs()
print("\nStatistiques du PSG:")
equipe2.afficherStatistiquesJoueurs()
