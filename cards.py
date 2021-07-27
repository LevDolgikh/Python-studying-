# Date: 26.07.2021
# Author: Lev Dolgikh

# <Блек-джек>
# Демонстрирует создание модуля для игры в <Блек-джек>

def gameSettings():
    """Метод описывающий правила игры"""
    print("""
        Игра 'Блек-Джек'
        В игре учавствует несколько игроков.
        Каждый игрок стремиться набрать 21 очко.
        Очки складываюьтся из номинала карт:
        Туз (А) - 1 или 11 очков, Король, дама, валет (K,Q,J) - 10 очков,
        2,3,4,5,6,7,8,9,10 - количество очков соотвествует номиналу цифры.
        Компьютер сначало сдает по 2 карты участникам игры, в том числе и себе,
        игрокам видны карты друг друга, но одна карта у компьютера(дилера) лежит рубашкой вверх.
        Далее каждый игрок по очереди тянет карту из колоды, пока сумма его очков не привысит 21.
        Если сумма очков в руке привысит 21, то игрок проигрывает.
        Если после одного круга, остались участники, то дилер раскрывает карты
        и раздает себе карты пока у него не станет 17 очков или больше, если дилер набирает более 21 очка,
        то выигрывают все игроки, в противном случае количество очков сравниватся с количеством очков дилера
        и выявляется побелитель. При одинаковом количестве очков объявляется ничья.
        """)

def askYesNo(question):
    """Задает вопрос с ответом да или нет"""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

class Card(object):
    """Класс под 1 карту"""
    
    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ("c", "d", "h", "s")
    
    def __init__(self, setRank, setSuit):
        """Инициализация объекта"""
        newRank = str(setRank).upper()
        newSuit = str(setSuit).lower()
        self.__rank = setRank
        self.__suit = setSuit

    def __str__(self):
        """Выводит номинал и масть карты"""
        rep = str(self.__rank) + str(self.__suit)
        return rep

    def cardPoints(self,score):
        """Подсчитывает очки карты"""
        score = int(score)
        points = 0
        if score <= 10 and self.__rank == "A":
            points = 11
        elif score > 10 and self.__rank == "A":
            points = 1
        elif self.__rank in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
            points = int(self.__rank)
        elif self.__rank in ("J","Q","K"):
            points = 10
        else:
            print("Ошибка подстчета очков карты")
        return points
    
    # Возвращают и устнавливают значения объектов класса
    @property
    def rank(self):
        return self.__rank

    @property
    def suit(self):
        return self.__suit

    @rank.setter
    def rank(self,newRank):
        newRank = str(newRank).upper()
        if newRank in self.RANKS:
            self.__rank = newRank
        else:
            print("Номикал карты не удалось изменить, введено неверное значение")

    @suit.setter
    def suit(self,newSuit):
        newSuit = str(newSuit).lower()
        if newSuit in self.SUITS:
            self.__suit = newSuit
        else:
            print("Масть карты не удалось изменить, введено неверное значение")

class FlippedCard(Card):
    """Перевернутая карта"""

    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ("c", "d", "h", "s")
   
    def __init__(self, card):
        """Инициализация перевернутой карты"""
        self.__rank = ""
        self.__suit = ""
        rank = str(card)[0]
        suit = str(card)[1]
        newRank = str(rank).upper()
        newSuit = str(suit).lower()
        self.__isFlipped = True
        if (rank in self.RANKS) and (suit in self.SUITS):  
            self.__rank = rank
            self.__suit = suit
        else:
            print("Введено неверное значение номикала или масти карты, установлено значение по умолчанию")

    def __str__(self):
        """Выводит номинал и масть карты"""
        rep = ""
        if self.__isFlipped:
            rep = "XX"
        else:
            rep = str(self.__rank) + str(self.__suit)
        return rep

    def flip(self):
        self.__isFlipped = not self.__isFlipped

    def cardPoints(self,score):
        """Подсчитывает очки карты"""
        score = int(score)
        points = 0
        if score <= 10 and self.__rank == "A":
            points = 11
        elif score > 10 and self.__rank == "A":
            points = 1
        elif self.__rank in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
            points = int(self.__rank)
        elif self.__rank in ("J","Q","K"):
            points = 10
        else:
            print("Ошибка подстчета очков карты")
        return points
            

class Hand(object):
    """Рука 1 игрока"""
    
    def __init__(self, playersName):
        """Инициализация объекта"""
        self.__name = playersName
        self.__cards = []
        
    def __str__(self):
        """Вывод карт руки на экран с подсчетом очков"""
        if str(self.__cards[0]) == "XX":
            if not self.__cards:
                rep = self.__name + ":\tВ руке нет карт"
            else:
                rep = self.__name + ":\t\t"
                for card in self.__cards:
                    rep += str(card) + "\t"
                rep += "(??)"
        else:
            if not self.__cards:
                rep = self.__name + ":\tВ руке нет карт"
            else:
                rep = self.__name + ":\t\t"
                for card in self.__cards:
                    rep += str(card) + "\t"
                rep += "(" + str(self.score()) + ")"
        return rep

    def addCard(self, card):
        """Добавляет карту в руку"""
        self.__cards.append(card)

    def clear(self):
        self.__cards = []

    def getCard(self, cardIndex):
        """Возвращает карту"""
        card = Card("A","h")
        if self.__cards:
            card = self.__cards[int(cardIndex)]
        else:
            print("Не удалось вернуть карту, ошибка работы программы")
        return card

    def setCard(self, card, index):
        """Ставит карту на место"""
        if index in range(0,len(self.__cards)):
            self.__cards[index] = card
        
    def score(self):
        """Вычисление очков карт в руке"""
        score = 0
        try:
            for card in self.__cards:
                score += card.cardPoints(score)
        except:
            print("Не удалось подсчитать счет игрока, в руке находятся карты несоотвествующего образца")
        return score

    def flipFirstCard(self):
        if self.__cards:
            firstCard = self.__cards[0]
            self.__cards[0] = FlippedCard(firstCard)
        else:
            print("Невозможно перевернуть карту, в руке нет карт")

    def unflipFirstCard(self):
        if self.__cards:
            self.__cards[0].flip()
        else:
            print("Невозможно перевернуть карту, в руке нет карт")

    @property
    def name(self):
        return self.__name
            
class Deck(Hand):
    """Колода"""

    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ("c", "d", "h", "s")
    
    def __init__(self):
        """Инициализация колоды"""
        self.__cards = []
        self.fill()
        self.shuffle()

    def __str__(self):
        """Вывод колоды на экран"""
        print("Использовать для отладки программы, т.к. отображение колоды при игре может повлиять на ход игры")
        rep = ""
        if not self.__cards:
            rep = "В колоде нет карт"
        else:
            for card in self.__cards:
                rep += str(card) + " "
        return rep
    
    def fill(self):
        self.clear()
        for rank in self.RANKS:
            for suit in self.SUITS:
                card = Card (rank,suit)
                self.__cards.append(card)

    def shuffle(self):
        import random
        if self.__cards:
            random.shuffle(self.__cards)

    def giveCards(self, hand, cards):
        for i in range(0,int(cards)):
            if self.__cards:
                card = self.__cards.pop(0)
                hand.addCard(card)
            else:
                print("В колоде нет карт") 

class Dealer(object):
    """Дилер игры (отвечает за механику игры и сам игровой процесс"""
    def __init__(self,playersNumber):
        """Инициализирует дилера"""
        self.__playersNumber = playersNumber
        self.__deck = Deck()
        self.__hands = []
        self.__dealerHand = None
        
    def __str__(self):
        """Выводит руки игроков на экран"""
        rep = "\nТекущий стол выглядит следующим образом:\n"
        if self.__hands and self.__dealerHand:
            for hand in self.__hands:
                rep += str(hand) + "\n"
            rep += str(self.__dealerHand)
        else:
            rep = "Игра еще не началась, запустите игру для отображения карт игроков"
        return rep

    def __createHands(self):
        """Запрашивает имена игроков и создает руки"""
        self.__clear()
        for i in range(0,self.__playersNumber):
            playersName = input("Введите имя игрока № " + str(i+1) + ": ")
            hand = Hand(playersName)
            self.__hands.append(hand)
        self.__dealerHand = Hand("Дилер")

    def __firstRound(self):
        """Первая раздача"""
        print("\nДилер раздает по 2 карты игрокам и себе")
        for hand in self.__hands:
            self.__deck.giveCards(hand,2)
        self.__deck.giveCards(self.__dealerHand,2)
        self.__dealerHand.flipFirstCard()
        print(self.__str__())

    def __drawCards(self):
        question = ""
        response = None
        for hand in self.__hands:
            response = None
            while response != "n":
                question = "\n" + hand.name + " будете брать еще карты? (Y/N): "
                response = askYesNo(question)
                if response == "y":
                    self.__deck.giveCards(hand,1)
                print(hand)
                if hand.score() > 21:
                    response = "n"
                    print(hand.name + " перебрал и проигрывает.")

    def __winner(self):
        winner = ""
        bestScore = 0
        playersLeft = []
        for hand in self.__hands:
            if hand.score() <= 21:
                playersLeft.append(hand)
        playersLeft.append(self.__dealerHand)
        self.__dealerHand.unflipFirstCard()
        if len(playersLeft) > 1:
            print("\nИгра продолжаеся между следующими участниками:")
            for hand in playersLeft:
                print(hand)
            print("\nДилер берет карты")
            while self.__dealerHand.score() < 17:
                self.__deck.giveCards(self.__dealerHand,1)
                print(self.__dealerHand)
            # Определение побелителя
            if self.__dealerHand.score() > 21:
                print("Дилер перебрал")
                winner = "игроки"
            else:
                for hand in playersLeft:
                    if hand.score() <= 21 and hand.score() > bestScore:
                        bestScore = hand.score()
                        winner = hand.name      
        else:
            winner = self.__dealerHand.name
        print("\nИтоговый счет игры: ")
        for hand in playersLeft:
            print(hand)
        print("\nПобедил: " + winner)   

    def startGame(self):
        gameSettings()
        self.__createHands()
        self.__firstRound()
        self.__drawCards()
        self.__winner()

    def __clear(self):
        self.__hands = []

if __name__ == "__main__":
    dealer = Dealer(2)
    dealer.startGame()
    print("Вы запустили модуль на прямую, его необходимо подключить к вашей программе")



