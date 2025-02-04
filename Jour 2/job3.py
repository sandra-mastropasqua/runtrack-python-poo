class Livre :
    def __init__(self, titre, auteur, nbPages, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, valeur):
        self.__titre = valeur

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, valeur):
        self.__auteur = valeur
    
    def get_nbPages(self):
        return self.__nbPages
    
    def set_nbPages(self, valeur):
        if valeur > 0:
            self.__nbPages = valeur
        else :
            print("Erreur")
    def verification(self):
        return self.__disponible is True

    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else :
            print("Le livre n'est pas dispo")

    def rendre(self):  
        if not self.verification():
            self_disponible = True
        else : 
            print("Le livre est disponible")

livre = Livre("Sandra","Gina", 451, False)
print(f"Titre : {livre.get_titre()}")
print(f"Auteur : {livre.get_auteur()}")
print(f"Nb de pages : {livre.get_nbPages()}")

print(f"Le livre est disponible : {livre.verification()}")

livre.emprunter()
print(f"Le livre est disponible : {livre.verification()}")
livre.emprunter()

livre.rendre()
print(f"Le livre est disponible : {livre.verification()}")
livre.rendre()
