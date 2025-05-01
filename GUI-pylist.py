from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import tkinter as tk

#Déclaration variable
def Ajout_tache():
    Demande = simpledialog.askstring("Ajout d'une nouvelle tâche","Entrez le nom de la tâche : ")
    if Demande:
        data.append(Demande)

def Afficher_tache():
    Top_fenêtre = Toplevel(root)
    Top_fenêtre.minsize(300, 250)
    text_data = "\n".join(f"{i}. {tache}" for i, tache in enumerate(data))
    Label(Top_fenêtre, text=text_data).pack()

def Supprimer_tache():
    Top_fenêtre = Toplevel(root)
    Top_fenêtre.minsize(300, 250)
    my_listbox = Listbox(Top_fenêtre)
    my_listbox.pack(pady=15)
    def suppression():
        selection = my_listbox.curselection()
        if selection:
            index = selection[0]
            my_listbox.delete(index)
            del data[index]
    for item in data:
        my_listbox.insert(END, item)
    my_button= Button(Top_fenêtre, text="Supprimer", command= suppression)
    my_button.pack(side=BOTTOM,pady=10)
        
def quitter_programme():
    root.destroy()



#initialisation de data
data = []

#Création fenëtre
root = Tk()

#création de la listbox


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
Bouton_Voir = Button(Boite_Bouton, text="Voir les tâches",command=Afficher_tache)
Bouton_Voir.pack()
Bouton_Supprimer = Button(Boite_Bouton, text="Supprimer les tâches",command=Supprimer_tache)
Bouton_Supprimer.pack()
Bouton_Quitter = Button(Boite_Bouton, text="Quitter programe",command=quitter_programme)
Bouton_Quitter.pack()

#Frame
Boite_Titre.pack()
Boite_Bouton.pack()

#Main loop
root.mainloop()
