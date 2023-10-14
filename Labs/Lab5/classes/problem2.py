class Shape:
    def area(self, a = 0):
        return a

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length


#x = Square(5)
#print(x.area())