class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    def __verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Carburant insuffisant pour démarrer.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")

ma_voiture = Voiture("Peugeot","208",2020, 35000)
print("En marche :", ma_voiture.get_en_marche())
ma_voiture.demarrer()
print("En marche :", ma_voiture.get_en_marche())  
ma_voiture.arreter()  
print("En marche :", ma_voiture.get_en_marche())  
print("Niveau du réservoir :", ma_voiture.get_reservoir())  
