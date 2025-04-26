#Pylist V1
#Axel INGRAO
#GPL Licence
#Functions 
def module_affichage():
    print("Bienvenue dans Pylist")
    print("Entrez ce que vous voulez faire :")
    print("1 = Ajoutez une tâche")
    print("2 = Voir les tâches")
    print("3 = supprimer une tâches")
    print("4 = Sortie")
#Déclation des variables
list = []
#appel affichage
module_affichage()
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
            break
        case _:
            print("Choix invalide...")