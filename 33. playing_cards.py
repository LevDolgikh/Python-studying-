# Date: 20.07.2021
# Author: Lev Dolgikh

# Карты
# Демонстрирует сочетание объектов

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

card1 = Card(rank = "A", suit = "c")
print(card1)
card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "3", suit = "c")
card4 = Card(rank = "4", suit = "c")
card5 = Card(rank = "5", suit = "c")
card6 = Card(rank = "6", suit = "c")
print(card2)
print(card3)
print(card4)
print(card5)
print(card6)

hand1 = Hand()
hand1.add(card1)
hand1.add(card2)
hand1.add(card3)
print(hand1)

hand2 = Hand()
hand2.add(card4)
hand2.add(card5)
hand2.add(card6)
print(hand2)

hand1.give(card1,hand2)
print(hand1)
print(hand2)

        
input("\n\nНажмите 'Enter', что бы выйти")



