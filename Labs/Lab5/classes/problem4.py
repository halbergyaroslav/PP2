import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f'OX coordinate: {self.x}, OY coordinate: {self.y}')
        
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
    def dist(self, a):
        return math.sqrt((a.x - self.x) * (a.x - self.x) + (a.y - self.y) * (a.y - self.y))
    

#a = Point(4, 3)
#b = Point(6, 2)

#a.show()
#b.show()

#b.move(0, 0)
#print(a.dist(b))