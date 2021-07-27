# Date: 27.07.2021
# Author: Lev Dolgikh
import cards
# <Блек-джек>
# Демонстрирует запуск модуля с игрой <Блек-джек>

def main():
    response = None
    while response != "n":
        players = int(input("Введите количество игроков <1-7>: "))
        if players in range (1,8):
            game = cards.Dealer(players)
            game.startGame()
        cards.askYesNo("Ходите сыграть еще раз (Y/N): "
                       
main()
input("\n\nНажмите 'Enter', что бы выйти")



