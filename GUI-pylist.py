from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import tkinter as tk

#Déclaration variable
def ajout_tache():
    demande = simpledialog.askstring("Ajout d'une nouvelle tâche","Entrez le nom de la tâche : ")
    if demande:
        data.append(demande)

def afficher_tache():
    top_fenetre = Toplevel(root)
    top_fenetre.minsize(300, 250)
    ### option GPT
    # text_data = "\n".join(f"{i}. {tache}" for i, tache in enumerate(data))
    ### option 1
    text_data = ""
    dataIndex = 0
    for dataValue in data:
        text_data = text_data + str(dataIndex) + ". " + dataValue + "\n"
        dataIndex = dataIndex + 1
    ###
    ### option 2
    #text_data = ""
    #for dataIndex, dataValue in enumerate(data):
    #    text_data = text_data + dataIndex + ". " + dataValue + "\n"
    #    dataIndex = dataIndex + 1
    ###
    Label(top_fenetre, text=text_data).pack()

def supprimer_tache():
    top_fenetre = Toplevel(root)
    top_fenetre.minsize(300, 250)
    my_listbox = Listbox(top_fenetre)
    my_listbox.pack(pady=15)
    def suppression():
        selection = my_listbox.curselection()
        if selection:
            index = selection[0]
            my_listbox.delete(index)
            del data[index]
    for item in data:
        my_listbox.insert(END, item)
    my_button= Button(top_fenetre, text="Supprimer", command= suppression)
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
root.minsize(350, 300)
root.maxsize(350, 300)

#Création boite_titre
boite_titre = Frame(root)
boite_bouton = Frame(root)

#label text
label_bienvenue = Label(master= boite_titre, text="Bienvenue dans Pylist GUI ", font="Helvetica 18 bold")
label_bienvenue.pack(pady= 15)

#Boutons
bouton_ajouter = Button(boite_bouton, text="Ajoutez une tâche", font="Helvetica 12" ,command=ajout_tache)
bouton_ajouter.pack(pady= 5)
bouton_voir = Button(boite_bouton, text="Voir les tâches",font="Helvetica 12" ,command=afficher_tache)
bouton_voir.pack(pady= 5)
bouton_supprimer = Button(boite_bouton, text="Supprimer les tâches",font="Helvetica 12" ,command=supprimer_tache)
bouton_supprimer.pack(pady= 5)
bouton_quitter = Button(boite_bouton, text="Quitter programe",font="Helvetica 12" ,command=quitter_programme)
bouton_quitter.pack(pady= 5)

#Frame
boite_titre.pack(side=TOP)
boite_bouton.pack()

#Main loop
root.mainloop()
