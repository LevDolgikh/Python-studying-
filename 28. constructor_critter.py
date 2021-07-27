# Date: 17.07.2021
# Author: Lev Dolgikh

# Зверюшка с конструктором
# Демонстрирует метод-конструктор

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self):
        print("Появилась на свет новая зверюшка!")
    def talk(self):
        print("Привет. Я зверюшка - экземпляр класса Critter.")

# основная часть
crit1 = Critter()
crit1.talk()
crit2 = Critter()
crit2.talk()

input("\n\nНажмите 'Enter', что бы выйти")



