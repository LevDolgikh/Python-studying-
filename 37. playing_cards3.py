# Date: 24.07.2021
# Author: Lev Dolgikh

# Карты 3.0
# Демонстрирует наследование в части переопределения методов

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

class UnprintableCard(Card):
    
    def __str__(self):
        return "<Нельзя напечатать>"

class PosotionableCard(Card):

    def __init__(self, rank, suit, faceUp = True):
        super(PosotionableCard, self).__init__(rank, suit)
        self.isFaceUp = faceUp
    def __str__(self):
        if self.isFaceUp:
            rep = super(PosotionableCard, self).__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        self.isFaceUp = not self.isFaceUp
        

card1 = Card("A","c")
card2 = UnprintableCard("A","d")
card3 = PosotionableCard("A","h")

print("Печатаю 1 карту")
print(card1)
print("Печатаю 2 карту")
print(card2)
print("Печатаю 3 карту")
print(card3)
print("Переворачиваю 3 карту")
card3.flip()
print("Печатаю 3 карту снова")
print(card3)
      
input("\n\nНажмите 'Enter', что бы выйти")



