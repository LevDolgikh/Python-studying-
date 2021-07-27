# Date: 17.07.2021
# Author: Lev Dolgikh

# Просто зверюшка
# Демонстрирует простейшие класс и объект

class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет. Я зверюшка - экземпляр класса Critter.")
# основная часть
crit = Critter()
crit.talk()

input("\n\nНажмите 'Enter', что бы выйти")



