# Date: 05.07.2021
# Author: Lev Dolgikh

# Рекорды
# Демонстрирует списочные методы

records = []
choice = None



while choice != 0:
    print ("Сделайте ваш выбор: \n0 - Выйти\n1 - Показать рекорды\n2 - Добавить рекорды\n3 - Удалить рекорды\n4 - Сортировать рекорды")
    choice = int(input ("Ваш выбор: "))
    if choice == 0:
           print ("До свидания!")
    elif choice == 1:
        print ("Рекорды: \n", records)
    elif choice == 2:
        newRecord = int(input ("Впишите свой рекор: "))
        records.append(newRecord)
    elif choice == 3:
        deleteRecordN = int(input("Введите номер рекорда, который хотите удалить: "))
        if deleteRecordN >= 0 and deleteRecordN < len(records):
            del records[deleteRecordN-1]
        else:
            print ("Введено неверное значение")
    elif choice == 4:
        records.sort(reverse=True)
        print ("Сортировка прошла успешно")
    else:
        print ("Извините, но такого пункта нет в меню")
input ("\nНажмите \"Enter\", что бы выйти")
