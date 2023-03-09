#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""

# Exo 1

"""
Chainage :  0 | 1 | 2 |  3 |    4    | 5 |  6 | 7 | 8 |    9    | 10
           22 |   | 2 | 36 | 26 -> 15|   | 50 |   |   | 9 -> 31 | 21

Ici tout les éléments de la table sont des listes chainées.

Sondage lineaire :  0 |  1 | 2 |  3 |  4 |  5 |  6 | 7 | 8 | 9 | 10
                   22 | 31 | 2 | 36 | 26 | 15 | 50 |   |   | 9 | 21

Pour le 31 les cases 9 et 10 sont prise donc on revient à la première case 
car on est en sondage linéaire donc la case 0 est prise 
et on a la case 1 qui n'est pas prise. On met 31 ici. 
"""

# Exo 2

class Noeud :
    """
    Cette classe crée l'élément noeud d'une liste chainée composer d'une valeur 
    et de l'adresse du noeud suivant s'il existe.
    """
    def __init__(self, valeur = None, pointeur = None):
        """
        Méthode d'initialisation d'un noeud.

        Args : valeur (Any, optionnal) : Valeur à ce noeud de la liste chainée.
               poiteur (Noeud, optional) : Prochain noeud de la liste chainée.
        """
        # Variables
        self.valeur = valeur
        self.pointeur = pointeur



class ListeChainee :
    """
    Cette classe crée une liste chainée composée de noeud.
    """
    def __init__(self):
        """
        Méthode d'initialisation de la classe. Crée une liste chainée vide.
        """
        # Variable
        self.head = Noeud()
        self.size = 0


    def inserer(self, valeur, num = 0):
        """
        Méthode qui permet d'inserer, à un endroit voulu ou à la fin, une valeur.

        Args : valeur (Any) : Valeur à inserer.
               num (int, optionnal) : Endroit où il faut inserer la valeur.
        """
        # Variables
        current_num = 0
        noeud_test = self.head

        # On vérifie si on demande une place précise.
        if num == 0:
            num = -1
        
        # Si on implémente la première valeur de la liste chainée
        if noeud_test.valeur == None:
            noeud_test.valeur = valeur
        else :
            if noeud_test.pointeur != None: # Vérification s'il n'y a pas de prochain noeud.
                while noeud_test.pointeur != None: # Itération jusqu'à l'endroit voulu.
                    if current_num == num-2: # Insertion à l'endroit voulu.
                        break
                    noeud_test = noeud_test.pointeur
                    current_num += 1
            noeud_test.pointeur = Noeud(valeur, noeud_test.pointeur) # Insertion                      
        self.size += 1
   
    def supprimer(self, num):
        """
        Méthode qui permet de suprimer un valeur à une certaine position.

        Args : num (int) : Position qui doit être supprimée.

        Returns : booleean : Indique si la suppréssion a été réalisé.
        """
        # Variables
        current_num = 0
        noeud_test = self.head

        # Vérification si la liste est assez grande
        if self.taille() >= num-1: 
            if noeud_test.pointeur != None:
                while noeud_test.pointeur != None: 
                    if current_num == num-1:
                        break
                    noeud_test_pre = noeud_test
                    noeud_test = noeud_test.pointeur
                    current_num += 1
                noeud_test_pre.pointeur = noeud_test.pointeur
                temp = noeud_test.valeur
            else :
                temp = noeud_test.valeur
                noeud_test.valeur = None
            return True, temp
        return False, None


    def rechercher(self, valeur):
        noeud_test = self.head
        if noeud_test.pointeur != None:
            while noeud_test.pointeur != None:
                if noeud_test.valeur == valeur:
                    return True
                noeud_test = noeud_test.pointeur
        return False
    
    def taille(self):
        return self.size
    
    def estVide(self):
        if self.head.valeur == None:
            return True
        return False

# Exo 3

class Pile:
    def __init__(self):
        self.pile = ListeChainee()

    def taille(self):
        return self.pile.taille()
    
    def estVide(self):
        return self.pile.estVide()
    
    def push(self,valeur):
        self.pile.inserer(valeur)

    def pop(self):
        return self.pile.supprimer(self.taille())
    
    def top(self):
        temp = self.pile.supprimer(self.taille())[1]
        self.push(temp)
        return temp


def validateurParenthesage(fichier):
    debut = ("{", "[", "<", "(")
    fin = ("}", "]", ">", ")")
    P = Pile()
    ligne = 1
    for lettre in fichier:
        if lettre == "\n":
            ligne += 1
        if lettre in debut:
            P.push(lettre)
        if lettre in fin:
            temp = fin.index(lettre)
            if debut[temp] == P.top():
                P.pop()
            else:
                return "Erreur de syntaxe à la ligne " + str(ligne)
    
    if P.estVide():
        return "Aucune erreur de syntaxe"
    return "Erreur de syntaxe à la ligne " + str(ligne)

# Exo 5

# 1/ [4, 8, 12]

# 2/ Un liste qui permet de retrouver des element a partir de leur indice (n° dans la liste)

def Josephus(n, k):
    ret = []
    for i in range(n):
        if (i+1) % k == 0 :
            ret.append(i+1)     
    return ret

print(Josephus(15, 4))




    