colors=["black","brown","red","yellow","green","blue"]
for i in range(10):
    guess=input("Угай цвет:")
    if guess in colors:
        print("Вы угадали!")
    else:
        print("Попробуй еще раз!")
