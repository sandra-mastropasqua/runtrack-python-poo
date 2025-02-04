class Cercle :
    def __init__(self,rayon):
        self.rayon = rayon
    def changerRayon(self,nouveaurayon):
        self.rayon = nouveaurayon
    def afficherInfos(self):
        print(self.rayon)
    def circonférence(self):
        return (self.rayon*2*3.14)
    def aire(self):
        return(self.rayon*self.rayon*3.14)
    def diametre(self):
        return(self.rayon*2)


cercle1 = Cercle(4)
cercle1.afficherInfos()
print(cercle1.circonférence())
print(cercle1.aire())
print(cercle1.diametre())
cercle2 = Cercle(7)
cercle2.afficherInfos()
print(cercle2.circonférence())
print(cercle2.aire())
print(cercle2.diametre())
