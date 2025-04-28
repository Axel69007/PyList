class ToDoList:

    def __init__(self, listToLoad = []):
        self._stringList = listToLoad

    def ClearTasks(self):
        self._stringList = []

    def AddNewTask(self, newStringTask):
        self._stringList.append(newStringTask)

    def RemoveTask(self, taskIndex):
        self._stringList.remove(self._stringList[int(taskIndex)])

    def GetTasksNumber(self):
        return len(self._stringList)
    
    def GetTaskByIndex(self, taskIndex):
        return self._stringList[taskIndex]

    def GetTasksInArray(self):
        return self._stringList
