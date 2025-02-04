class Rectangle : 
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, valeur):
        self.__longueur = valeur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, valeur):
        self.__largeur = valeur
    
mesure = Rectangle(10,5)
print(f"Longueur initial : {mesure.get_longueur()}")
print(f"Largeur initiale : {mesure.get_largeur()}")

mesure.set_longueur(15)
mesure.set_largeur(8)

print(f"Nouvelle longueur : {mesure.get_longueur()}")
print(f"Nouvelle largeur : {mesure.get_largeur()}")

