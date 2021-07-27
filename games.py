# Date: 24.07.2021
# Author: Lev Dolgikh

# Игры
# Демонстрирует создание модуля

class Player(object):
    """Участник игры"""
    def __init__(self,name,score = 0):
        self.name = name
        self.score = score
    def __str__(self):
        rep = ""
        rep += "\tИгрок " + self.name + " имеет счет: " + str(self.score) + "\n"
        return rep
def askYesNo(question):
    """Задает вопрос с ответом да или нет"""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

def askNumber(question, low, high):
    """Просит ввести число из заданного диапазона"""
    response = None
    while response not in range(low,high+1):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("Вы запустили этот модуль напрямую а не импортировали его")
    input("Нажмите 'Enter', что бы выйти")
    
