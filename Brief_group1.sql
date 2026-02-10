CREATE DATABASE gestion_boutique_db;
SHOW DATABASES;
USE gestion_boutique_db;
CREATE TABLE Produits (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nom VARCHAR(100) NOT NULL,
prix VARCHAR(50) NOT NULL,
quantite_initiale INT NOT NULL
);
SHOW TABLES;
describe Produits;
CREATE TABLE Categories (
id_categorie INT NOT NULL  AUTO_INCREMENT PRIMARY KEY,
nom_categorie VARCHAR(100) NOT NULL
);
DESCRIBE Categories;
select * from Produits;

ALTER TABLE Produits ADD id_categorie INT NOT NULL,
ADD FOREIGN KEY (id_categorie) REFERENCES Categories (id_categorie);
SELECT * FROM Categories;