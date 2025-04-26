#Pylist V1
#Axel INGRAO
#GPL Licence
from datetime import datetime
#Functions 
def Module_affichage():
    print("Bienvenue dans Pylist")
    print("Entrez ce que vous voulez faire :")
    print("1 = Ajoutez une tâche")
    print("2 = Voir les tâches")
    print("3 = supprimer une tâches")
    print("4 = Sortie")
def Module_fichier(Liste_Saved):
    Date_AJD=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    Nom_fichier=str(Date_AJD)+".txt"
    with open(Nom_fichier,"w") as fichier:
        fichier.write(Liste_Saved)
#Déclation des variables
list = []
#Appel fonction
Module_affichage()
#Boucle infinie du programme
while True :
    Choix=(input("Entrez votre choix : "))
    match Choix:
        case "1":
            list.append(input("entrez le nom de la tâche : "))
        case "2":
            Compteur_liste=0
            for i in list :
                print(str(Compteur_liste)+" "+ i)
                Compteur_liste=Compteur_liste+1
        case"3":
            Choix_suppression=input("Entrez l'index de la tâches à supprimer : ")
            list.remove(list[int(Choix_suppression)])
        case"4":
            Module_fichier(str(list))
            break
        case _:
            print("Choix invalide...")