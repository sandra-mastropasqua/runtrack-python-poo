class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population
    
    def ajouter_habitant(self):
        self.__population += 1
    
    def get_population(self):
        return self.__population
    
    def get_nom(self):
        return self.__nom

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_habitant()
    
    def __str__(self):
        return f"{self.__nom}, {self.__age} ans, habitant à {self.__ville.get_nom()}"


paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)


print(f"Population de {paris.get_nom()} : {paris.get_population()}")
print(f"Population de {marseille.get_nom()} : {marseille.get_population()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(john)
print(myrtille)
print(chloe)


print(f"Population de {paris.get_nom()} après arrivée des nouveaux habitants : {paris.get_population()}")
print(f"Population de {marseille.get_nom()} après arrivée des nouveaux habitants : {marseille.get_population()}")





