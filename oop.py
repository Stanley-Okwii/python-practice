class Oop:
    def __init__(self, myinput):
        self.myinput = myinput
    
    def getString(self):
        input = self.myinput
        return input
    
    def printString(self):
        upperCase = self.myinput.upper() 
        print(upperCase)

City = Oop("New York")
City.printString()
