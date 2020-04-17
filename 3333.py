class Ending:
    ends=["","а","ы"]
    def __init__(self,number):
        self.number=number
    def change_end(self):
        self.number=int(self.number)
        if (self.number//10)%10==1:
            return ends[0]
        else:
            if self.number%10==0 or 5<=self.number%10<=9:
                print(ends[1])
            elif self.number%10==1:
                print(ends[2])
            elif 1<=self.number%10<=4:
                print(ends[2])
    def __repr__(self):
        print(self.change_end)
s=Ending(100)
print(s.change_end)
            
            
