# Date: 17.07.2021
# Author: Lev Dolgikh

# Зверюшка с атрибутами
# Демонстрирует создание атрибутов объекта и доступ к ним

class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod
    def status():
        print("\nBcero зверюшек сейчас" , Critter.total)
    def __init__(self,name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        Critter.total += 1
    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep
    def talk(self):
        print("Привет. Я зверюшка, меня зовут ", self.name, "\n")

# основная часть
crit1 = Critter("Мурзик")
crit1.talk()
crit2 = Critter("Бобик")
crit2.talk()
print(crit1)
print(crit2)
print("Доступ к атрибуту crit.name: ", crit1.name, "\n")
Critter.status()

input("\n\nНажмите 'Enter', что бы выйти")



