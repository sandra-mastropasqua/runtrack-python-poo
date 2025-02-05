class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = {}  
        self.__statut = "en cours"

   
    def get_numero_commande(self):
        return self.__numero_commande

    def get_statut(self):
        return self.__statut

    def get_plats(self):
        return self.__plats.copy()

    
    def ajouter_plat(self, nom_plat, prix):
        if self.__statut == "en cours":
            self.__plats[nom_plat] = {"prix": prix}
        else:
            print("Impossible d'ajouter un plat à une commande terminée ou annulée.")

   
    def annuler_commande(self):
        if self.__statut == "en cours":
            self.__statut = "annulée"
            self.__plats.clear()
        else:
            print("La commande ne peut pas être annulée.")

    
    def __calculer_total(self):
        return sum(plat["prix"] for plat in self.__plats.values())

    
    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande} - Statut: {self.__statut}")
        for plat, details in self.__plats.items():
            print(f"{plat}: {details['prix']} €")
        print(f"Total à payer: {self.__calculer_total()} €")

    
    def calculer_tva(self, taux=20):
        return self.__calculer_total() * (taux / 100)

if __name__ == "__main__":
    commande1 = Commande(101)
    commande1.ajouter_plat("Pizza", 12.5)
    commande1.ajouter_plat("Pâtes", 9.0)
    commande1.afficher_commande()
    print(f"TVA (20%) : {commande1.calculer_tva()} €")
    commande1.annuler_commande()
    commande1.afficher_commande()