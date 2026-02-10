import mysql.connector
from mysql.connector import errorcode


configuration = {
    'host' : 'localhost',
    'user': 'fatou',
    'password': 'Fatoumata02022026',
    'database': 'gestion_boutique_db'

}
try:
    connexion = mysql.connector.connect(**configuration)
    moncurseur = connexion.cursor()
    print("connexion bien etablie")

except mysql.connector.Error as erreur:
    if erreur.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erreur: nom d'utilisateur ou le mot de passe est incorrect")
    elif erreur.errno ==errorcode.ER_BAD_DB_ERROR:
        print("La base de donnees n'existe pas")
    else:
        print(f"Erreur MYSQL: {erreur}")

# CREATION DE LA AJOUT_CATEGORIE
def ajout_categorie():
    nom_categorie = input("Entrer le nom de la categorie du produit: ")
    requete = "INSERT INTO Categories (nom_categorie) VALUES (%s)" 
    moncurseur.execute(requete,(nom_categorie,))
    connexion.commit()
    resultats = moncurseur.fetchall()
    print(resultats)

# FONCTION AFFICHER CATEGORIE
def affiche_categorie():
    requete = "SELECT * FROM Categories"
    moncurseur.execute(requete)
    resultats = moncurseur.fetchall()
    print(resultats)

# # FONCTION POUR AJOUTER UN PRODUIT
def ajout_produit():
    nom= input("Entrer le nom du produit: ").replace(" ", "")
    while True:
        if nom.isalpha():
            print("saisie valide")
            prix = (input("Entrer le prix: "))
            while True:
                if prix.isdigit():
                    print("saisie du prix valide")
                   
                    quantite_initiale = input("Entrer la quantite du produit: ").replace(" ", "")
                    while True:
                        if quantite_initiale.isdigit():
                            print("Saisie de la quantite du produit valide")
                            affiche_categorie()
                            id_categorie = int(input("Entrer l'id de la categorie: "))

                            break
                        else:
                            quantite_initiale = input("Saisie invalide veuillez entrer la quantite du produit: ").replace(" ", "")
                    break
                else:
                    print("----prix invalide")
                    prix = input("Entrer le prix: ").replace(" ","")
            break
        else:
            print("saisie invalide veuillez ressayer")
            nom= input("Entrer le nom du produit").replace(" ","")

    requete = "INSERT INTO Produits (nom, prix, quantite_initiale,id_categorie) VALUES (%s, %s, %s, %s)"

    moncurseur.execute(requete,(nom, prix, quantite_initiale,id_categorie),)
    connexion.commit()
    
    print(f"nom du produit: {nom} | prix: {prix} | quantite: {quantite_initiale} | ID categorie: {id_categorie}")
    
# CREATION DE LA FONCTION AFFICHAGE STOCK
def affichage_stock():
    requete = "SELECT * FROM Produits"
    moncurseur.execute(requete)
    resultats = moncurseur.fetchall()
    for i,produit in enumerate(resultats, start=1):
        print(f"{i}.  {produit[1]}     {produit[2]}     {produit[3]}")

def mise_a_jour_vente():
    affichage_stock()
    id =int(input("Entrer l'ID du produit a mettre a jour: "))
    quantite_vendue = int(input("Entrer la quantite du produit a ajouter: "))
    #verification stock initial
    requete_verif = "SELECT quantite_initiale FROM Produits WHERE id = %s"
   
    moncurseur.execute(requete_verif, (id,))
    resultat = moncurseur.fetchone()
    if resultat:
        stock_actuel = resultat[0]
        if stock_actuel >= quantite_vendue:

            requete = "UPDATE Produits SET quantite_initiale = quantite_initiale - %s WHERE id = %s"
            moncurseur.execute(requete,(quantite_vendue,id))
            
            connexion.commit()
            print(f"Vente reussie, nouveau_stock : {stock_actuel-quantite_vendue}")
        else:
            print("stock disponible insuffisant")
    else:
        print("produit introuvable")

def mise_a_jour_arrivage():
    affichage_stock()
    id =int(input("Entrer la quantite du produit a mettre a jour: "))
    quantite_vendue = int(input("Entrer la quantite du produit a ajouter: "))
    requete = "UPDATE Produits SET quantite_initiale = quantite_initiale + %s WHERE id = %s"
    valeur = (quantite_vendue,id)
    moncurseur.execute(requete,valeur)
    connexion.commit()
    print("quantite mise a jour")

# MODIFICATION DE LA QUANTITE DE STOCK
def modifier_quantite():
    print("1. Vente")
    print("2. Arrivage")
    choix= int(input("Choix: "))
    if choix ==1:
        mise_a_jour_vente()
    elif choix==2:
        mise_a_jour_arrivage()
    else:
        print("choix invalide")
        menu()
def rechercher_produit(nom):
    requete = "SELECT * FROM Produits WHERE nom = %s"
    moncurseur.execute(requete,(nom,))
    resultats = moncurseur.fetchall()
    if resultats:
        for produit in resultats:
            print(f"{produit[0]}  | {produit[1]}  |  {produit[2]} | {produit[3]}")
    else:
        print("produit non trouve")

# Creation de la fonction supprimer un produit
def supprimer_produit(id):
    requete = "DELETE FROM Produits Where id = %s"
    moncurseur.execute(requete,(id,))
    connexion.commit()
    print(f"Le produit avec l'ID: {id} a ete supprime")

# FONCTION PRODUIT_PLUS_CHER
def produit_plus_cher():
    requete = "SELECT nom, prix FROM Produits ORDER BY prix DESC LIMIT 1"
    moncurseur.execute(requete)
    resultat = moncurseur.fetchone()
    # connexion.commit()
    print(resultat)

def totale_financiere():
    requete = "SELECT SUM(prix) FROM Produits"
    moncurseur.execute(requete)
    resultat = moncurseur.fetchall()
    print(f"{resultat} FCFA")

# FONCTION PRODUIT PAR CATEGORIE
def produit_categorie():
    requete = """SELECT  c.nom_categorie, GROUP_CONCAT(p.nom SEPARATOR ",") as PRODUITS FROM Categories c JOIN Produits p ON p.id_categorie = c.id_categorie GROUP BY c.nom_categorie """
    moncurseur.execute(requete)
    resultat = moncurseur.fetchall()
    for categorie, produit in resultat:
        print(f"{categorie}: {produit}")
    
# CREATION DE LA FONCTION DASHBOARD
def dashboard():
    print("1. Le produit le plus cher")
    print("2. La valeur totale financiere de tout le stock")
    print("3. Les produits par categorie")
    choix = int(input("Choix: "))
    if choix==1:
        produit_plus_cher()
    elif choix==2:
        totale_financiere()
    else:
        produit_categorie()

# CREATION DE LA FONCTION MENU
def menu():
    while True:
        print("1. Ajouter un produit")
        print("2. Affichage de tous les produits en stock")
        print("3. Ajouter une categorie")
        print("4. afficher liste categorie")
        print("5. Modification de la quantite de stock")
        print("6. Rechercher un produit")
        print("7. Supprimer un produit")
        print("8. Dashboard")
        print("9. Quitter")
        Choix = int (input("Choisissez une option: "))
        match Choix:
            case 1:
                ajout_produit()
            case 2:
                affichage_stock()
            case 3:
               ajout_categorie()
            case 4:
                affiche_categorie()
            case 5:
                modifier_quantite()
            case 6:
                nom= input("Entrer le nom du produit").replace(" ", "")
                rechercher_produit(nom)
            case 7:
                affichage_stock()
                id = int(input("Entrer l'ID du produit a supprimer: "))
                supprimer_produit(id)
            case 8:
                dashboard()
            case 9:
                print("A la prochaine")
                break
            case _:
                print("---Choix invalide")
                print('--------------------------------------')
    return



def fermeture():
    if connexion and connexion.is_connected():
        moncurseur.close()
        connexion.close()
    print("fermuture reussi")

menu()
fermeture()