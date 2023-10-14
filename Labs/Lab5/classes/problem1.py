class First_Class:
    def __init__(self, s = ''):
        self.s = s
        
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())


#line = First_Class()
#line.getString()
#line.printString()