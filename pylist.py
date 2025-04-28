#Pylist V1
#Axel INGRAO
#GPL Licence
import os
from tkinter import *
#Déclaration des fonctions 
#Module simple d'affichage
def Module_affichage():
    print("-----------------------------------")
    print("Bienvenue dans Pylist")
    print("-----------------------------------")
    print("Entrez ce que vous voulez faire :")
    print("1 = Ajoutez une tâche")
    print("2 = Voir les tâches")
    print("3 = supprimer une tâches")
    print("4 = Sortie")
#Module création du fichier config
def Module_creation():
    with open("config.cfg","w") as fichier:
        print("Création du fichier config.cfg")
#Module écriture du tableau data dans le fichier cfg
def Module_fichier(Liste_Saved):
    with open("config.cfg","w") as fichier:
        for tache in Liste_Saved:
            fichier.write(tache + "\n")
#Module lecture du fichier config.cfg 
def Module_lecture():
    with open("config.cfg") as fichier1:
        Raw_Lignes=(fichier1.readlines())
        Lignes=[]
        for ligne in Raw_Lignes:
            Lignes.append(ligne.strip())
        return Lignes
#Vérification de la présence de config.cfg
if not os.path.isfile("config.cfg"):
    Module_creation()
#Initialisation du tableau data avec la lecture du fichier
data=Module_lecture()
#Appel fonction
Module_affichage()
#Boucle infinie du programme
while True :
    Choix=(input("Entrez votre choix : "))
    match Choix:
        case "1":
            data.append(input("entrez le nom de la tâche : "))
        case "2":
            Compteur_liste=0
            for i in data :
                print(str(Compteur_liste)+". "+ i)
                Compteur_liste=Compteur_liste+1
        case"3":
            Choix_suppression=input("Entrez l'index de la tâches à supprimer : ")
            data.remove(data[int(Choix_suppression)])
        case"4":
            Module_fichier(data)
            break
        case _:
            print("Choix invalide...")