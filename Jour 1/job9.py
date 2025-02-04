class Produit : 
    def __init__(self):
        self.nom = ""
        self.prixHT = 0
        self.TVA = 0
    def CalculerPrixTTC(self):
        return (self.prixHT * self.TVA /100)
    def afficher(self):
        return self.CalculerPrixTTC()
    def changernom(self,nouveaunom):
        self.nom = nouveaunom
    def changerprix(self, nouveauprix):
        self.prixHT = nouveauprix
    def afficherNom(self):
        return self.nom
    def afficherPrix(self):
        return self.prixHT
    def afficherTVA(self):
        return self.TVA 

truc = Produit()
truc.nom = "emilie"
truc.prixHT = 120
truc.TVA = 20

print(truc.afficher())
truc.changerprix(60)
print(truc.afficherPrix())
print(truc.afficher())

truc.changernom("emilie")
print(truc.afficherNom())





