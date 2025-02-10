class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"{self.name} en {self.material}"

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "Mât": Part("Mât", "Bois"),
            "Coque": Part("Coque", "Acier"),
            "Voile": Part("Voile", "Tissu")
        }
        self.history = []
        self.history_file = "histo.txt"

    def log_history(self, event):
        self.history.append(event)
        with open(self.history_file, "a") as file:
            file.write(event + "\n")

    def display_state(self):
        print(f"État du bateau {self.name}:")
        for part in self.__parts.values():
            print(f" - {part}")

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
            self.log_history(f"Remplacement de {part_name} par {new_part}")
        else:
            print("Pièce non trouvée.")

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
            self.log_history(f"Modification de {part_name} en {new_material}")
        else:
            print("Pièce non trouvée.")

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        print(f"Vitesse maximale du {self.name}: {self.max_speed} noeuds")

def menu():
    ship = RacingShip("Black Pearl", 35)
    while True:
        print("\n1. Afficher l'état du bateau")
        print("2. Remplacer une pièce")
        print("3. Modifier le matériau d'une pièce")
        print("4. Afficher la vitesse maximale")
        print("5. Afficher l'historique des modifications")
        print("6. Quitter")
        choix = input("Votre choix: ")

        if choix == "1":
            ship.display_state()
        elif choix == "2":
            part_name = input("Nom de la pièce à remplacer: ")
            new_name = input("Nom de la nouvelle pièce: ")
            new_material = input("Matériau de la nouvelle pièce: ")
            ship.replace_part(part_name, Part(new_name, new_material))
        elif choix == "3":
            part_name = input("Nom de la pièce à modifier: ")
            new_material = input("Nouveau matériau: ")
            ship.change_part(part_name, new_material)
        elif choix == "4":
            ship.display_speed()
        elif choix == "5":
            print("\nHistorique des modifications:")
            with open(ship.history_file, "r") as file:
                print(file.read())
        elif choix == "6":
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()
