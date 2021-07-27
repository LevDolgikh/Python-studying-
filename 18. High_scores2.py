# Date: 05.07.2021
# Author: Lev Dolgikh

# Рекорды 2
# Демонстрирует вложенные последовательности

records = []
choice = None

print ("Рекорды 2.0")

while choice != 0:
    print ("Сделайте ваш выбор: \n0 - Выйти\n1 - Показать рекорды\n2 - Добавить рекорды")
    choice = int(input ("Ваш выбор: "))
    if choice == 0:
           print ("До свидания!")
    elif choice == 1:
        print ("Рекорды: \n")
        print ("Имя\t\t РЕЗУЛЬТАТ")
        for entry in records:
            score, name = entry
            print (name, "\t\t", score)
    elif choice == 2:
        newRecordPlayer = input ("Впишите имя игрока: ")
        newRecordScore = int(input ("Впишите результат: "))
        records.append((newRecordScore, newRecordPlayer))
        records.sort(reverse=True)
        records = records[:5]
    else:
        print ("Извините, но такого пункта нет в меню")
input ("\nНажмите \"Enter\", что бы выйти")
