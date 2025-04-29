from tkinter import *
from tkinter import ttk
from tkinter import simpledialog

#Déclaration variable
def Ajout_tache():
    Demande = simpledialog.askstring("Ajout d'une nouvelle tâche","Entrez le nom de la tâche : ")
    if Demande:
        data.append(Demande)

def Afficher_tâche():
    Top_fenêtre = Toplevel(root)
    Top_fenêtre.minsize(300, 250)
    Label(Top_fenêtre, text=data).pack()


data = []

#Création fenëtre
root = Tk()

#Paramètre fenêtre
root.title("PyList GUI V1")
root.minsize(300, 250)

#Création Boite_Titre
Boite_Titre = Frame(root)
Boite_Bouton = Frame(root)

#label text
label_bienvenue = Label(Boite_Titre, text="Bienvenue dans Pylist GUI \n ----------------------------------", font=("Helvetica"))
label_bienvenue.pack()

#Boutons
Bouton_Ajouter = Button(Boite_Bouton, text="Ajoutez une tâche",command=Ajout_tache)
Bouton_Ajouter.pack()
Bouton_Voir = Button(Boite_Bouton, text="Voir les tâches",command=Afficher_tâche)
Bouton_Voir.pack()
Bouton_Supprimer = Button(Boite_Bouton, text="Supprimer les tâches")
Bouton_Supprimer.pack()
Bouton_Quitter = Button(Boite_Bouton, text="Quitter programe")
Bouton_Quitter.pack()

#Frame
Boite_Titre.pack()
Boite_Bouton.pack()

#Main loop
root.mainloop()
