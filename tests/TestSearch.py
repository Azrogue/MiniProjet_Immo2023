import tkinter as tk

class RechercheBiens(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Recherche de biens")
        
        # Création de la barre de recherche
        self.label_critere = tk.Label(self.master, text="Critère de recherche:")
        self.label_critere.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        
        self.criteres = ["Année de construction", "Type de bien", "Commune", "Superficie couverte", "Nature de la gestion", "Prix"]
        self.liste_critere = tk.StringVar(self.master)
        self.liste_critere.set(self.criteres[0])
        self.dropdown_critere = tk.OptionMenu(self.master, self.liste_critere, *self.criteres)
        self.dropdown_critere.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        
        self.label_recherche = tk.Label(self.master, text="Termes de recherche:")
        self.label_recherche.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        
        self.entry_recherche = tk.Entry(self.master)
        self.entry_recherche.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        
        self.button_recherche = tk.Button(self.master, text="Rechercher", command=self.rechercher)
        self.button_recherche.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    
    def rechercher(self):
        critere = self.liste_critere.get()
        recherche = self.entry_recherche.get()
        # Ajouter ici le code pour la recherche en fonction du critère et du terme de recherche entrés
        
if __name__ == "__main__":
    root = tk.Tk()
    recherche_biens = RechercheBiens(root)
    recherche_biens.mainloop()
