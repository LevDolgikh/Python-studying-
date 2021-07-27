# Date: 24.07.2021
# Author: Lev Dolgikh

# Простая игра
# Демонстрирует импорт модулей

import games, random

print("Добро пожаловать в самую простую игру!")
again = None
while again != "n":
    players = []
    num = games.askNumber("Сколько игроков учавствует(2 - 5): ", 2, 5)
    for i in range(0,num):
        name = input("Имя игрока: ")
        score = random.randint(1,100)
        player = games.Player (name, score)
        players.append(player)
    print("Результаты игры:")
    for player in players:
        print(player)
    again = games.askYesNo("Продолжить игру ('y' или 'n'): ")
input("Нажмите 'Enter', что бы выйти")
    
