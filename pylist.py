#Pylist V1
#Axel INGRAO
#GPL Licence
import os
#Déclaration des fonctions 
#Module simple d'affichage
def module_affichage():
    print("-----------------------------------")
    print("Bienvenue dans Pylist")
    print("-----------------------------------")
    print("Entrez ce que vous voulez faire :")
    print("1 = Ajoutez une tâche")
    print("2 = Voir les tâches")
    print("3 = supprimer une tâches")
    print("4 = Sortie")
#Module création du fichier config
def module_creation():
    with open("config.cfg","w") as fichier:
        print("Création du fichier config.cfg")
#Module écriture du tableau data dans le fichier cfg
def module_fichier(Liste_Saved):
    with open("config.cfg","w") as fichier:
        for tache in Liste_Saved:
            fichier.write(tache + "\n")
#Module lecture du fichier config.cfg 
def module_lecture():
    with open("config.cfg") as fichier1:
        Raw_Lignes=(fichier1.readlines())
        Lignes=[]
        for ligne in Raw_Lignes:
            Lignes.append(ligne.strip())
        return Lignes
#Vérification de la présence de config.cfg
if not os.path.isfile("config.cfg"):
    module_creation()
#Initialisation du tableau data avec la lecture du fichier
data=module_lecture()
#Appel fonction
module_affichage()
#Boucle infinie du programme
while True :
    choix=(input("Entrez votre choix : "))
    match choix:
        case "1":
            data.append(input("entrez le nom de la tâche : "))
        case "2":
            compteur_liste=0
            for i in data :
                print(str(compteur_liste)+". "+ i)
                compteur_liste=compteur_liste+1
        case"3":
            choix_suppression=input("Entrez l'index de la tâches à supprimer : ")
            data.remove(data[int(choix_suppression)])
        case"4":
            module_fichier(data)
            break
        case _:
            print("Choix invalide...")