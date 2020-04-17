class Square(): #нужныли скобки, если да, то зачем?
    def __init__ (self, s1,s2):
        self.s1=s1
        self.s2=s2
sq1=Square(10,7)
sq2=Square(12,7)
print(sq1.s1 is sq2.s1)
print(sq1.s1 is sq2.s2)
print(sq1.s2 is sq2.s1)
print(sq1.s2 is sq2.s2)

