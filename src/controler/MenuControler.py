from enum import Enum
import sys

from dataHandler.ToDoList import ToDoList
from database.FileDataBase import FileHandler

class ActionDetails:
    def __init__(self, key, details):
        self.key = key
        self.details = details


class MenuActions(Enum):
    ADD_NEW_TASK = ActionDetails("1", "Ajouter une tache")
    DISPLAY_TASKS = ActionDetails("2", "Afficher les taches")
    REMOVE_TASK = ActionDetails("3", "Supprimer une tache")
    QUIT = ActionDetails("4", "Quitter le programme")

class MenuControler:

    def __init__(self, userInterface):
        self._userInterface = userInterface
        self._database = FileHandler("others\config.cfg")

        if(self._database.isDatabaseAvailable()):
            self._toDoList = ToDoList(self._database.getDataAsArray())
        else:
            self._toDoList = ToDoList()

        self.displayUserChoices()

    def __run__(self):
        userChoice = ""
        while userChoice != MenuActions.QUIT.value.key :
            userChoice = self.waitUserAction()
            self.makeAnAction(userChoice)
            
    def displayUserChoices(self, arrayOfOptions = []):
        self._userInterface.displayString("Entrez ce que vous voulez faire :")
        for option in MenuActions:
            self._userInterface.displayString(option.value.key + " = " + option.value.details)

    def waitUserAction(self, userChoice = "Entrez votre choix : "):
        return self._userInterface.waitUserInputAsString(userChoice)
    
    def makeAnAction(self, actionToMake):
        match actionToMake:

            case MenuActions.ADD_NEW_TASK.value.key:
                newTask = self.waitUserAction("Entrez le nom de la tâche : ")
                self._toDoList.AddNewTask(newTask)

            case MenuActions.DISPLAY_TASKS.value.key:
                taskNumber=0
                for task in self._toDoList.GetTasksInArray() :
                    self._userInterface.displayString(str(taskNumber) + " : " + task)
                    taskNumber=taskNumber+1

            case MenuActions.REMOVE_TASK.value.key:
                Choix_suppression = self._userInterface.waitUserInputAsString("Entrez ne numéro de la tâches à supprimer : ")
                self._toDoList.RemoveTask(Choix_suppression)

            case MenuActions.QUIT.value.key:
                self._database.saveDataFromArray(self._toDoList.GetTasksInArray())
                sys.exit(0)

            case _:
                self._userInterface.displayString("Choix invalide...")