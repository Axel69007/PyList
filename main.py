#Pylist V1
#Axel INGRAO
#GPL Licence
#Functions 
def module_affichage():
    print("Bienvenue dans Pylist")
    print("Entrez ce que vous voulez faire :")
    print("1 = Ajoutez une tâche")
    print("2 = Voir les tâches")
    print("3 = Sortie")
#Déclation des variables
list = []
#appel affichage
module_affichage()
#Boucle infinie du programme
while True :
    Choix=(input("Entrez votre choix : "))
    if Choix =="1":
        list.append(input("entrez le nom de la tâche : "))
    if Choix =="2":
        for i in list :
            print(i)
    if Choix == "3":
        break
