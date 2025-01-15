from historique import Historique

class Calculatrice:
    """
    Classe principale pour effectuer des calculs.
    """

    def __init__(self):
        """
        Initialise une instance de la classe Calculatrice.

        Attributs :
        -----------
        historique : list
            Une liste vide qui stocke l'historique des calculs.
        historique_manager : Historique
            Une instance de la classe Historique pour gérer l'historique.
        resultat : None
            Initialise le résultat à None, indiquant qu'aucun calcul n'a été effectué au départ.
        """
        self.historique = []  # Liste pour stocker l'historique des calculs
        self.historique_manager = Historique()  # Gestionnaire de l'historique
        self.resultat = None  # Aucun résultat initial

    def addition(self, num1, num2):
        """Effectue l'addition de deux nombres"""
        return num1 + num2

    def soustraction(self, num1, num2):
        """Effectue la soustraction de deux nombres"""
        return num1 - num2

    def multiplication(self, num1, num2):
        """Effectue la multiplication de deux nombres"""
        return num1 * num2

    def division(self, num1, num2):
        """Effectue la division de deux nombres et gère la division par zéro"""
        if num2 == 0:
            return "Erreur: division par zéro"  # Gestion de la division par zéro
        return num1 / num2

    def demander_nombre(self, prompt):
        """
        Demande à l'utilisateur d'entrer un nombre et valide l'entrée.
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide.")

    def demander_operation(self):
        """
        Demande à l'utilisateur de choisir une opération valide.
        """
        while True:
            operateur = input("Entrez une opération (+, -, *, /) : ")
            if operateur in ("+", "-", "*", "/"):
                return operateur
            print("Erreur: Veuillez entrer un opérateur valide.")

    def convertir_si_entier(self, valeur):
        """
        Convertit un float en int si possible.
        """
        if isinstance(valeur, (int, float)) and valeur == int(valeur):
            return int(valeur)
        return valeur

    def executer_calcul(self, num1, num2, operateur):
        """
        Exécute l'opération choisie avec num1 et num2 en fonction de l'opérateur.
        """
        if operateur == "+":
            return self.addition(num1, num2)
        elif operateur == "-":
            return self.soustraction(num1, num2)
        elif operateur == "*":
            return self.multiplication(num1, num2)
        elif operateur == "/":
            return self.division(num1, num2)

    def ajouter_historique(self, num1, operateur, num2, resultat):
        """
        Ajoute le calcul effectué et son résultat à l'historique.
        """
        self.historique.append({
            'num1': num1,
            'operation': operateur,
            'num2': num2,
            'resultat': resultat
        })

    def menu_historique(self):
        """
        Affiche les options relatives à l'historique des calculs et gère les choix de l'utilisateur.
        """
        print("\nOption de l'historique :")
        print("1. Voir l'historique")
        print("2. Effacer l'historique")
        print("3. Faire un calcul")
        choix_historique = input("Choisissez une option (1-lire/2-effacer/3-calculer) : ")
        if choix_historique == "1":
            self.historique_manager.lire()
            return True  # Continuer après avoir vu l'historique
        elif choix_historique == "2":
            self.historique_manager.effacer()
            return True  # Continuer après avoir effacé l'historique
        elif choix_historique == "3":
            return False  # Sortir du menu pour calculer
        else:
            print("Option invalide. Veuillez choisir 1, 2 ou 3.")
            return True
        
    

    def run(self):
        """
        Exécute la calculatrice en boucle.
        """
        while True:
            print("\n=== CALCULATRICE ===")

            # Menu historique
            print("\n=== MENU HISTORIQUE ===")
            continuer_menu = self.menu_historique()
            if continuer_menu:
                continue

            # Réutilisation du dernier résultat
            if self.resultat is not None:
                utiliser_resultat = input(f"Votre dernier résultat était {self.resultat}. Voulez-vous l'utiliser ? (o/n) : ").lower()
                if utiliser_resultat == "o":
                    num1 = self.resultat
                else:
                    num1 = self.demander_nombre("Entrez le premier nombre : ")
            else:
                num1 = self.demander_nombre("Entrez le premier nombre : ")

            operateur = self.demander_operation()
            num2 = self.demander_nombre("Entrez le second nombre : ")

            # Conversion si nécessaire
            num1 = self.convertir_si_entier(num1)
            num2 = self.convertir_si_entier(num2)

            # Calcul du résultat
            self.resultat = self.executer_calcul(num1, num2, operateur)
            self.resultat = self.convertir_si_entier(self.resultat)

            print(f"Résultat : {self.resultat}")

            # Ajout à l'historique
            self.ajouter_historique(num1, operateur, num2, self.resultat)
            self.historique_manager.enregistrer(self.historique)

            # Demande de continuer ou quitter complètement
            continuer = input("\nVoulez-vous effectuer un tout nouveau calcul ? (o/n) : ").lower()
            if continuer not in ["o", "oui"]:
                print("Au revoir !")
                break
