class Rectangle():
    def __init__(self,len,weidth):
        self.len = len
        self.weidth = weidth
    def calculate_perimeter(self):
        return (self.len+self.weidth)*2
class Square(Rectangle):
    def change_size(self):
        if self.len<0:
            self.len+=1
            print(self.len)
rec1=Rectangle(10,3)
print(rec1.calculate_perimeter())
squ1=Square(-10,10)
print(squ1.calculate_perimeter())

