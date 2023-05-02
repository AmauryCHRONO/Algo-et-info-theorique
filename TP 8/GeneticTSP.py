import os
import TP8
import random
from GeneticTSPGui import PVC_Genetique_GUI

class PVC_Genetique:

    def __init__(self, list_villes, taille = 40, generation = 100, elitism = True, mut_proba = 0.3):
        self.list_villes = list_villes
        self.taille = taille
        self.generation = generation
        self.elitism = elitism
        self.mut_proba = mut_proba
        self.GUI = PVC_Genetique_GUI(list_villes)
    
    def croiser(self, parent1, parent2):
        enfant = TP8.Trajet()

        moitier = len(parent1.list_villes)//2
        list_enfant = parent1.list_villes[:moitier]
        for ville in parent2.list_villes:
            if ville not in list_enfant:
                list_enfant.append(ville)

        enfant.list_villes = list_enfant
        
        if enfant.est_valide:
            return enfant
        return TP8.Trajet()

    def muter(self, trajet):
        if random.random()<self.mut_proba:
            for i in range(random.randint(0, (len(trajet.list_villes)-1)//4)):
                mut = trajet.list_villes.pop(random.randint(0, len(trajet.list_villes)-1))
                trajet.list_villes.insert(random.randint(0, len(trajet.list_villes)-1), mut)
                trajet.calc_longueur()
        return trajet

    def selectionner(self, population):
        meilleur = population.meilleur()[:3]
        return meilleur

    def evolution(self, population):
        parents = self.selectionner(population)
        if self.elitism :
            enfant = self.croiser(parents[0], parents[0])
        else:
            enfant = self.croiser(parents[0], parents[1])

        new_population = TP8.Population()
        for iteration in range(len(population.list_trajet)):
            enfant_mut = self.muter(enfant)
            new_population.ajouter(enfant_mut)

        return new_population

    def executer(self):
        afficher = True
        meilleur = []
        population = TP8.Population()
        population.initialiser(self.taille, self.list_villes)
        meilleur_trajet = population.meilleur()[0]
        meilleur_trajet_curent = meilleur_trajet
    
        for generation in range(self.generation):
            print("hello")
            old_population = population
            if population.meilleur()[0].longueur < meilleur_trajet.longueur :
                meilleur_trajet = population.meilleur()[0]
                meilleur_trajet_curent = population.meilleur()[0]
                meilleur.append(meilleur_trajet)
                old_population = population
                population = self.evolution(population)
            else:
                meilleur_trajet_curent = population.meilleur()[0]
                population = self.evolution(old_population)
            if afficher :
                self.GUI.afficher(meilleur_trajet, meilleur_trajet_curent, False)
        self.GUI.window.mainloop()



    def clear_term(self):
        os.system('cls' if os.name=='nt' else 'clear')
    
def main():
    test = PVC_Genetique(list_villes=TP8.lire_csv("30.csv"))
    test.executer()
if __name__ == "__main__":
    main()