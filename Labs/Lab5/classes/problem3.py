from problem2 import Shape

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

#x = Rectangle(4, 5)
#print(x.area())