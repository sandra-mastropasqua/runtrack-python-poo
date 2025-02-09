class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Compte n°{self.__numero} - Titulaire: {self.__prenom} {self.__nom} - Solde: {self.__solde}€")
    
    def afficherSolde(self):
        print(f"Solde actuel: {self.__solde}€")
    
    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué. Nouveau solde: {self.__solde}€")
    
    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde: {self.__solde}€")
    
    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.05  
            print(f"Agios appliqués. Nouveau solde: {self.__solde:.2f}€")
    
    def virement(self, compte_destinataire, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Virement impossible, solde insuffisant.")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant}€ effectué vers le compte {compte_destinataire.__numero}.")


compte1 = CompteBancaire("12345", "Dupont", "Jean", 1000)
compte2 = CompteBancaire("67890", "Martin", "Sophie", -200, decouvert=True)


compte1.afficher()
compte2.afficher()


compte1.virement(compte2, 200)


compte1.afficherSolde()
compte2.afficherSolde()
