# Date: 20.07.2021
# Author: Lev Dolgikh

# Карты 2.0
# Демонстрирует расширение класса через наследование

class Card(object):
    """Одна игральная карта"""
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """Рука одного игрока"""
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<пусто>"
        return rep
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, otherHand):
        self.cards.remove(card)
        otherHand.add(card)

class Deck(Hand):
    """Колода игральных карт"""
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, perHand = 1):
        for rounds in range(perHand):
            for hand in hands:
                if self.cards:
                    topCard = self.cards[0]
                    self.give(topCard,hand)
                else:
                    print("Не могу дать карту, карты закончились")
            
    
print("Создаем колоду:")    
deck1 = Deck()
print(deck1)

print("Наполняем колоду картами:")
deck1.populate()
print(deck1)

print("Мешаем колоду:")
deck1.shuffle()
print(deck1)

myHand = Hand()
yourHand = Hand()

print("Раздаем карты для 2-х игроков")
hands = [myHand,yourHand]
deck1.deal(hands,1)
print("Раздача завершена:")
print("Моя рука: ", myHand)
print("Твоя рука: ", yourHand)
      
input("\n\nНажмите 'Enter', что бы выйти")



