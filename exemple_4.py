for i in range (10):
    x=input("Задайте х:")
    x=int(x)
    y=input("Задайте у:")
    y=int(y)
    def f(x,y):
        return x**y
    print ("f(x,y)=x^y = ",f(x,y))
