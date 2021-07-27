# Date: 17.07.2021
# Author: Lev Dolgikh

# Закрытая зверюшка
# Демонстрирует закрытые переменные и методы

class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod
    def __status():
        print("\nBcero зверюшек сейчас" , Critter.total)
    def __init__(self, name, mood):
        print("Появилась на свет новая зверюшка!")
        self.__name = name
        self.__mood = mood
        Critter.total += 1
    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.__name + "\n"
        return rep
    def talk(self):
        Critter.__status()
        print("Привет. Я зверюшка, меня зовут ", self.__name)
        print("Моё настроение сейчас: ", self.__mood, "\n")
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, newName):
        if newName == "":
            print( "Имя зверюшки не может быть пустой строкой.")
        else:
            self.__name = newName
            print("Имя успешно изменено.")

# основная часть

crit = Critter("Борис", "Да все в целом окей")
crit.talk()
print(crit.name)
crit.name = "Волобуй"

input("\n\nНажмите 'Enter', что бы выйти")



