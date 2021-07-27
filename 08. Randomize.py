# Date: 29.06.2021
# Author: Lev Dolgikh
import random
# Случайности
# Демонстрирует генерацию случайных чисел

print ("""

        Добро пожаловать в игру \"Случайное число\"!
Я загадал натуральное число, от 1 до 100, опробуешь его отгадать?
            Чем меньше попыток, тем лучше!

""")

input ("\nНажмите \"Enter\", что бы продолжить")

print ("\nПроверяю механизмы генерации случайных чисел. Проверка завершена")
randomDig1 = random.randint (1,10)
randomDig2 = random.randrange(10)+1
yourPassword = random.randint (1000,9999)
hiddenNumber = random.randint (1,100)
yourNumber = "";
tryCount = 0;
print ("Проверяю везенье участников игры: ", randomDig1, " баллов из 10")
print ("Проверяю своё везенье: ", randomDig1, " баллов из 10")
print ("Ваш пароль для данной игры: ", yourPassword, " ,не забудьте, это важно (нет)")

getPassword = int(input("Для проверки введите пароль для игры. "))
if getPassword == yourPassword:
    print ("Проверка успешно пройдена, начнем играть!")
    while yourNumber != hiddenNumber:
        yourNumber = int(input("Введите ваше число "))
        tryCount += 1
        if yourNumber == hiddenNumber:
            print ("Поздравляю! Вы угадали с ", tryCount, " попытки")
        elif yourNumber > hiddenNumber:
            print ("Ваше значение больше загаданного!")
        elif yourNumber < hiddenNumber:
            print ("Ваше значение меньше загаданного!")
        else:
            print ("Сбой программы! ПОВТОРЯЮ! СБОЙ ПРОГРАММЫ")
else:
    print ("ДОСТУП ЗАКРЫТ!")

input ("\nНажмите \"Enter\", что бы выйти")
