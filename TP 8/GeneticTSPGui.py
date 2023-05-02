from tkinter import *

class PVC_Genetique_GUI(object):
    """
    Runs the application
    """
    def __init__(self,liste_villes):
        self.liste_villes = liste_villes
        self.generation = 0
        
        # Initiates a window object & sets its title
        self.window = Tk()
        self.window.wm_title("Génération 0")

        # initiates two canvases, one for current and one for best
        self.canvas_current = Canvas(self.window, height=300, width=300)
        self.canvas_best = Canvas(self.window, height=300, width=300)

        # Initiates two labels
        self.canvas_current_title = Label(self.window, text="Meilleur trajet de la génération courante :")
        self.canvas_best_title = Label(self.window, text="Meilleur trajet trouvé jusqu'ici :")

        # Initiates a status bar with a string
        self.stat_tk_txt = StringVar()
        self.status_label = Label(self.window, textvariable=self.stat_tk_txt, relief=SUNKEN, anchor=W)

        # creates dots for the cities on both of the canvases
        for city in liste_villes:
            self.canvas_current.create_oval(city.x-2, city.y-2, city.x + 2, city.y + 2, fill='blue')
            self.canvas_best.create_oval(city.x-2, city.y-2, city.x + 2, city.y + 2, fill='blue')

        # Packs all the widgets (physically creates them and places them in order)
        self.canvas_current_title.pack()
        self.canvas_current.pack()
        self.canvas_best_title.pack()
        self.canvas_best.pack()
        self.status_label.pack(side=BOTTOM, fill=X)

        # Runs the main window loop
        self.window.update()

    def afficher(self, meilleur, courant, pas = 1, afficher_noms = False):
        self.generation += 1
        if self.generation == 1:
            self.initial = courant.longueur
            if afficher_noms:
                for v in self.liste_villes:
                    self.canvas_best.create_text(v.x - 2, v.y - 5, text=v.nom, fill="black", font=('Helvetica 8'))
                    self.canvas_current.create_text(v.x - 2, v.y - 5, text=v.nom, fill="black", font=('Helvetica 8'))

        self.window.wm_title("Génération {0}".format(self.generation))
        self.update_canvas(self.canvas_best, meilleur, 'green')
        if self.generation % pas == 0:
            self.update_canvas(self.canvas_current, courant, 'red')

        self.stat_tk_txt.set('Trajet initial {0:.2f}    Meilleur trajet = {1:.2f}'.format(self.initial, meilleur.longueur))
        self.status_label.pack()
        self.status_label.update_idletasks()
        

        

    def update_canvas(self, the_canvas, trajet, color):
        # deletes all current items with tag 'path'
        the_canvas.delete('path')

        # loops through the route
        for i in range(len(trajet.list_villes)):

            # similar to i+1 but will loop around at the end
            next_i = i-len(trajet.list_villes)+1

            # creates the line from city to city
            the_canvas.create_line(trajet.list_villes[i].x,
                                trajet.list_villes[i].y,
                                trajet.list_villes[next_i].x,
                                trajet.list_villes[next_i].y,
                                tags=("path"),
                                fill=color)

            # Packs and updates the canvas
            the_canvas.pack()
            the_canvas.update_idletasks()
    
    def GA_loop(self,n_generations,pop_size, graph=False):
        return