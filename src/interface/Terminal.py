class Terminal:

    def __init__(self):
        pass

    def displayString(self, stringToDisplay):
        print(stringToDisplay)

    def displayArrayOfString(self, arrayOfString):
        for stringData in arrayOfString:
            print(stringData)

    def waitUserInputAsString(self, messageToDiplay):
        return input(messageToDiplay)