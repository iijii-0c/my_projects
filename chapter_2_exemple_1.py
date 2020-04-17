import math
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius
circle1=Circle(10)
print (circle1.area())
print(circle1.radius)
