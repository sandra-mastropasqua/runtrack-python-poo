class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0  
        self.__level = "Insuffisant"  

    def add_credits(self, nombre):
        if nombre > 0:
            self.__credits += nombre
            self.__level = self.__student_eval() 
        else:
            print("Erreur : le nombre de crédits doit être supérieur à zéro.")
    
    def get_credits(self):
        return self.__credits


    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Identifiant : {self.__numero_etudiant}")
        print(f"Niveau : {self.__level}")


etudiant = Student("Doe", "John", 145)


etudiant.add_credits(10)
etudiant.add_credits(8)
etudiant.add_credits(12)

print(f"Le nombre de crédits de John Doe est de {etudiant.get_credits()} points")

etudiant.student_info()



