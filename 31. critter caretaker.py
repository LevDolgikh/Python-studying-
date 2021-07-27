# Date: 18.07.2021
# Author: Lev Dolgikh

# Игра с питомцем
# Демонстрирует работу с классами и объектами классов

def playerChoice():
    """Проверка значения, введеного игроком"""
    theChoice = input("Ваш выбор: ")
    try:
        theChoice = int(theChoice)
        if theChoice not in range(0,4):
            print("Ошибка ввода. Попробуйте еще раз")
            theChoice = None
    except ValueError:
        print("Ошибка ввода. Попробуйте еще раз")
        theChoice = None
    return theChoice

def getPetName():
    """Принимает и проверяет имя питомца"""
    petName = ""
    while petName == "" or petName == " ":
        petName = input("Как вы назовете своего питомца: ")
        if petName == "" or petName == " ":
            print("Введите корректное имя питомца")
    return petName

class Pet(object):
    """Класс питомца"""
    def __init__(self, petName):
        self.__name = petName
        self.__mood = 100
        self.__fullness = 100

    def __str__(self):
        petInformation = "\nВаш питомец " + self.name + " имеет следующее состояние:"
        petInformation += "\nНастроение: " + str(self.mood)
        petInformation += "\nСытость: " + str(self.fullness)
        return petInformation

    def petStatus(self):
        self.__action()
        if self.mood >= 80 or self.fullness >= 80:
            print("Меня зовут ", self.name, " и сейчас я чувствую себя отлично!")
        elif (self.mood >= 60 and self.mood < 80) or (self.fullness >= 60  and self.fullness < 80):
            print("Меня зовут ", self.name, " и сейчас я чувствую себя хорошо!")
        elif (self.mood >= 40 and self.mood < 60) or (self.fullness >= 40  and self.fullness < 60):
            print("Меня зовут ", self.name, " и сейчас я чувствую себя нормально.")
        elif (self.mood >= 20  and self.mood < 40) or (self.fullness >= 20 and self.fullness < 40):
            print("Меня зовут ", self.name, " и сейчас я чувствую себя плохо!")
        elif (self.mood >= 10 and self.mood < 20) or (self.fullness >= 10  and self.fullness < 20):
            print("Меня зовут ", self.name, " и сейчас я чувствую себя очень плохо!")
        elif self.mood == 0 or self.fullness == 0:
            print("Из-за плохой заботы ваш питомец сбежал от вас! Заведите следующего! :)")

    def feed(self):
        print("Вы покормили своего питомца ", self.name)
        self.__action()
        if self.fullness != 0:
            self.__fullness += 30
        if self.fullness > 100:
            print("Настолько объелся, что больше не в ходит!")
            self.fullness = 100
        elif self.fullness >= 90 and self.fullness <=100:
            print("Питомец полностью сыт!")
        elif self.fullness >= 70 and self.fullness < 90:
            print("Питомец покушал и доволен")
        elif self.fullness >= 40 and self.fullness < 70:
            print("Питомец еще поел бы чуть чуть")
        elif self.fullness > 0 and self.fullness < 40:
            print("Питомец все еще голоден")
        elif self.fullness == 0 :
            print("Увы, ваш питомец сбежал от вас, решил что на свободе найти еду больше шансов, чем с вами")

    def play(self):
        print("Вы играете со своим питомцем ", self.name)
        self.__action()
        if self.mood != 0:
            self.__mood += 30
        if self.mood > 100:
            print("Ваш питомец в восторге!")
            self.mood = 100
        elif self.mood >= 90 and self.mood <=100:
            print("Питомец очень рад что вы с ним играете")
        elif self.mood >= 70 and self.mood < 90:
            print("Питомец хорошо наигрался")
        elif self.mood >= 40 and self.mood < 70:
            print("Питомец поиграл бы еще чуть чуть")
        elif self.mood > 0 and self.mood < 40:
            print("Питомцу недостаточно вашего внимания")
        elif self.mood == 0 :
            print("Увы, ваш питомец сбежал от вас, решил что на свободе ему будет веселее, чем с вами")            

    def __action(self):
        self.mood -= 10
        self.fullness -= 10
        
    @property
    def name(self):
        return self.__name

    @property
    def mood(self):
        return self.__mood    

    @property
    def fullness(self):
        return self.__fullness

    @name.setter
    def name(self, newName):
        if newName == "":
            print("Имя питомца не может быть пустым!")
        else:
            self.__name = newName

    @mood.setter
    def mood(self, newMood):
        try:
            newMood = int(newMood)
            if newMood >= 0 and newMood <= 100:
                self.__mood = newMood
            else:
                print("Введено неверное значение настроения")
        except ValueError:
            print("ОШИБКА: Введите целое число от 0 до 100")

    @fullness.setter
    def fullness(self, newFullness):
        try:
            newFullness = int(newFullness)
            if newFullness >= 0 and newFullness <= 100:
                self.__fullness = newFullness
            else:
                print("Введено неверное значение сытости")
        except ValueError:
            print("ОШИБКА: Введите целое число от 0 до 100")
            
def main():
    """Основная фукция программы"""
    petName = getPetName()
    pet = Pet (petName)

    choice = None

    while choice != 0:
        print("""

            Мой питомец (введите соотвествующий пункт меню):
            0 - Выйти
            1 - Узнать о самочувствии питомца
            2 - Покормить питомца
            3 - Поиграть с питомцем
            
            """)

        choice = playerChoice()
        if choice == 0:
            print("Спасибо за игру")
        elif choice == 1:
            pet.petStatus()
        elif choice == 2:
            pet.feed()
        elif choice == 3:
            pet.play()
            
main()
input("\n\nНажмите 'Enter', что бы выйти")



