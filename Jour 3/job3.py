class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut
    
    def marquerCommeFinie(self):
        self.statut = "terminée"
    
    def __str__(self):
        return f"{self.titre} - {self.description} [{self.statut}]"

class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache):
        self.taches.append(tache)
    
    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]
    
    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquerCommeFinie()
    
    def afficherListe(self):
        return [str(tache) for tache in self.taches]
    
    def filterListe(self, statut):
        return [str(tache) for tache in self.taches if tache.statut == statut]


todo_list = ListeDeTaches()

tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Réviser Python", "Travailler sur les classes et objets")
tache3 = Tache("Sport", "Faire 30 minutes de course")

todo_list.ajouterTache(tache1)
todo_list.ajouterTache(tache2)
todo_list.ajouterTache(tache3)

todo_list.marquerCommeFinie("Réviser Python")
todo_list.supprimerTache("Sport")

print("Toutes les tâches:", todo_list.afficherListe())
print("Tâches à faire:", todo_list.filterListe("à faire"))
