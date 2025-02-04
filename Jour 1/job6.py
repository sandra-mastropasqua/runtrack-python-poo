class Animal :
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self,nom):
        self.prenom = nom

animal1 = Animal()
print(f"Age de l'animal : {animal1.age}")
animal1.vieillir()
print(f"L'âge de l'animal : {animal1.age}")
animal1.nommer("Luna")
print(f"L'animal se nomme {animal1.prenom}")
