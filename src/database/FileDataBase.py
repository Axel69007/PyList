import os

class FileHandler:

    def __init__(self, filePath):
        self.filePath = filePath

    def isDatabaseAvailable(self):
        return os.path.isfile(self.filePath)

    def getDataAsArray(self):
        with open(self.filePath, "r") as localFile:
            Raw_Lignes=(localFile.readlines())
            Lignes=[]
            for ligne in Raw_Lignes:
                Lignes.append(ligne.strip())
            return Lignes
        
    def saveDataFromArray(self, listToSave):
        with open(self.filePath, "w") as localFile:
            for data in listToSave:
                localFile.write(data + '\n')
    
