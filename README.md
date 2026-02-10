 -- Configuration de la Base de Données: gestion_boutique_db

Description

Cette base de données permet de gérer une boutique en stockant :

-   Les **produits**
-   Les **catégories de produits**
-   Le lien entre produits et catégories

Prérequis

Avant de commencer, il faut :

-   Installer **MySQL**
-   Installer **MySQL Workbench** (ou autre outil SQL facultatif on travailler directement sur le terminal)
-   Installer une qui nous permet de connecter la base de donnees et le programme python(dans notre cas mysql-connector-python)

Étapes de Configuration

-Création de la base de données

  CREATE DATABASE gestion_boutique_db;


-Vérifier la création

  SHOW DATABASES;

-Sélectionner la base de données

  USE gestion_boutique_db;


-Création de la table: Produits


CREATE TABLE Produits (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prix VARCHAR(50) NOT NULL,
    quantite_initiale INT NOT NULL
);

-Vérifier la table Produits


SHOW TABLES;
DESCRIBE Produits;

-Création de la table Categories

CREATE TABLE Categories (
    id_categorie INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom_categorie VARCHAR(100) NOT NULL
);

-Vérifier la table Categories

DESCRIBE Categories;

-Ajout de la relation entre Produits et Catégories


  ALTER TABLE Produits 
  ADD id_categorie INT NOT NULL,
  ADD FOREIGN KEY (id_categorie) REFERENCES Categories (id_categorie);

-Vérification des données

  SELECT * FROM Produits;
  SELECT * FROM Categories;

-Structure de la Base de Données

  Categories
  -----------
  id_categorie (PK)
  nom_categorie

  Produits
  -----------
  id (PK)
  nom
  prix
  quantite_initiale
  id_categorie (FK)

-Relation entre les tables

  -Une catégorie peut contenir plusieurs produits
  -Un produit appartient à une seule catégorie

