from random import shuffle  #Импорт функции перемешивающей элементы списка.
class Card:                 #Создание класса "Карты"
    suits=["пикей","червей","бубей","треф"] #Создание переменной,включающей в себя список мастей.
    values=["None","None","2","3","4","5","6","7","8","9","10","валета","даму","короля","туза"] #Создание переменной, включающей в себя номиналы карт.
    def __init__(self,v,s):#Инициализация объектов класса "Карты", включающие в себя 2 параметра
        self.value=v #Инициализация первого параметра объектов класса "Карты"
        self.suit=s#Инициализация второго параметра объектов класса "Карты"
    def __lt__(self, other): #Инициализация "волшебного" метода в классе "Карты", позволяющего сравнивать объекты в классе, по какому-либо параметру
        if self.value < other.value: #Вызов метода (условия), осуществляющего выполнение определенного действия, при выполнении условия, содержащегося в теле метода и объявление параметра объекта
                                    #класса по которому осуществляет сравнение метод "__lt__"
            return True #Действие, выполняемое при соответствии условия, содержащегося в теле метода???
        if self.value == other.value: #Вызов метода, осуществляющего выполнение определенного действия, при выполнении условия, содержащегося в теле метода
            if self.suit < other.suit: #Объявление параметра объекта по которому осуществляется вторичное сравнение объектов класса, при равенстве первичных параметров
                return True #Действие, выполняемое при соответствии условия, содержащегося в теле метода???
            else: #Вызов подметода, выполняющего определенные действия, при невыполнении условия, содержащегося в теле метода.
                return False #Действие, выполняемое при соответствии условия, содержащегося в теле подметода
        return False
   
    def __repr__ (self): #Инициализация "волшебного" метода в классе "Карты", позволяющего выводить строку, содержащую значения, записанных в память параметров объекта класса
        return self.values[self.value]+" "+self.suits[self.suit]
class Deck: #Создание класса "Колода"
    def __init__(self): #Инициализация объектов класса "Колода"
        self.cards=[] #Создание пустого списка(колоды), в который будут добавляться карты, при их создании
        for i in range (2,15):#вызов метода, осуществляющего перебор элементов в заданоном списке(диапазоне)
            for j in range(4):#вызов метода, осуществляющего перебор элементов в заданоном списке(диапазоне)
                self.cards.append(Card(i,j))#Добавление нового элемента в список "cards". Добавляемый элемент - это объект в классе "Card"
        shuffle(self.cards)#Перемешивание элементов списка "self.cards"
    def rm_card(self): #Инициализация метода, осуществляющего удаление последнего элемента из списка "self.card"
        if len (self.cards)==0: #Вызов метода, выполняющего подсчет количества элементов в списке "self.card" и сравнение этого количества с нулем
            return #Действие, выполняемое при соответствии условия, содержащегося в теле метода???
        return self.cards.pop() #Действие, выполняемое в методе "rm_card".(Удаление последнего элемента из списка "self.card")
class Player:
    def __init__(self,name):
        self.wins=0
        self.card= None
        self.name=name
class Game:
    def __init__(self):
        name1 = input ("Имя игрока 1:")
        name2 = input ("Имя игрока 2:")
        self.deck=Deck()
        self.p1 = Player(name1)
        self.p2= Player(name2)
    def wins (self,winner):
        w="{} забирает карты"
        w=w.format(winner)
        print(w)
    def draw (self,p1n,p1c,p2n,p2c):
        d="{} кладет {}, а {} кладет {}"
        d=d.format(p1n,p1c,p2n,p2c)
        print(d)
    def play_game(self):
        cards=self.deck.cards
        print("Поехали!")
        while len(cards)>=2:
            end1=len(self.deck.cards)
            end2=end1%10
            end3=(end1//10)%10
            if end3==1:
                a=""
            else:
                if end2==0:
                    a=""
                elif end2==1:
                    a="а"
                elif 1<end2<=4:
                    a="ы"
                elif 5<end2<=9:
                    a=""
            print("Текущий счет {}-{} : {}-{}. В колоде осталось {} карт{}".\
                  format(self.p1.name,self.p1.wins,self.p2.name,self.p2.wins,\
                         len(self.deck.cards),a))
            m="Нажмите Х для выхода. Нажмите любую другую клавишу для продолжения игры."
            print("{} кон.".format(27-len(self.deck.cards)//2))
            response=input(m)
            if response =='Х':
                break
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins +=1
                self.wins(self.p2.name)
            win=self.winner(self.p1,self.p2)
        print("В колоде не осталось карт. Игра окончена. Итоговый счет {}-{}:{}-{}.".\
              format(self.p1.name,self.p1.wins,self.p2.name,self.p2.wins,\
                         len(self.deck.cards),a))
        if win=="Ничья!":
            print("{}".format(win))
        else:
            print("{} выиграл!".format(win))
    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            return p2.name
        return "Ничья!"
game = Game()
game.play_game()
