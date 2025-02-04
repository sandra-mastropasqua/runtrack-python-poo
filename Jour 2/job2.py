class Livre :
    def __init__(self, titre, auteur, nbPages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbPages = nbPages
    
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
    
livre = Livre("Sandra","Gina", 451)
print(f"Titre : {livre.get_titre()}")
print(f"Auteur : {livre.get_auteur()}")
print(f"Nb de pages : {livre.get_nbPages()}")

livre.set_titre("Lola")
livre.set_auteur("Jean")
livre.set_nbPages(80)

print(f"Titre : {livre.get_titre()}")
print(f"Auteur : {livre.get_auteur()}")
print(f"Nb de pages : {livre.get_nbPages()}")

livre.set_nbPages(-1)

