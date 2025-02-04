class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        print(f"Le résultat de l'addition est {self.nombre1 + self.nombre2}")

operation1 = Operation(12, 13)
print(f"Le nombre1 est {operation1.nombre1} Le nombre2 est {operation1.nombre2}")
operation1.addition()