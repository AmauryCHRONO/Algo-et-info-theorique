#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI
"""

# Bibliothèques importées
import math
import random
import csv

# Classe ville
class Ville:
    def __init__(self, nom, x, y):
        self.nom = nom
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.nom)

    def distance_vers(self, autre_ville):
        return math.sqrt(((self.x - autre_ville.x) ** 2) + ((self.y - autre_ville.y) ** 2))


class Trajet:
    def __init__(self, list_villes = []):
        if list_villes != []:
            random.shuffle(list_villes)

        self.list_villes = list_villes
        self.longueur = 0

        if self.est_valide():
            self.calc_longueur()

    def __str__(self):
        tmp = "["
        for ville in self.list_villes:
            tmp += str(ville)+", "
        tmp = tmp[:-2] + "]"
        return tmp
        
    def calc_longueur(self):
        for num, ville in enumerate(self.list_villes):
            self.longueur += ville.distance_vers(self.list_villes[num - 1])

    def est_valide(self):
        for ville_1 in self.list_villes:
            count = 0
            for ville_2 in self.list_villes:
                if ville_1.x == ville_2.x and ville_1.y == ville_2.y:
                    count += 1
            if count > 1 :
                return False
        return True
        

class Population:
    def __init__(self):
        self.list_trajet = []
    
    def __str__(self):
        tmp = "["
        for trajet in self.list_trajet:
            tmp += str(trajet)+", "
        tmp = tmp[:-2] + "]"
        return tmp
    
    def initialiser(self, taille, list_villes):
        for iteration in range(taille):
            self.list_trajet.append(Trajet(list_villes))
    
    def ajouter(self, trajet):
        self.list_trajet.append(trajet)

    def meilleur(self):
        self.list_trajet.sort(key=lambda trajet: trajet.longueur)
        return self.list_trajet


# Fonction qui génere une liste de n villes de coordonnées aléatoire
def generer_villes(nb_villes = 20):
    return [Ville(i, random.randint(0, 300), random.randint(0, 300)) for i in range(nb_villes)]

# Fonction qui génere une liste de villes à partir d'un fichier .csv
def lire_csv(nom_fichier):
    list_villes = []
    with open(nom_fichier, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            list_villes.append(Ville(int(row[0]), int(row[1]), int(row[2])))
    
    return list_villes


