# Date: 06.07.2021
# Author: Lev Dolgikh

# Переводчик с гикского на русский
# Демонстрирует использование словарей

geek = { "404": "Не знать, не владеть информацией. От сообщения об ошибке 404 'Страница не найдена'.",
         "Googling": "Гугление. Поиск в сети сведений о ком-либо.",
         "Keyboard Plaque": "Мусор, который скапливается в клавиатуре компьютера"}

choice = None

while choice !=0:
    print(
        """
        Переводчик с гикского на русский:
        0 - Выйти
        1 - Найти толкование термина
        2 - Добавить термин
        3 - Изменить толкование
        4 - Удалить термин
        """
        )
    choice = int(input("Ваш выбор: "))
    
    if choice == 0:
        print("Спасибо за участие! Всего хорошего")
    elif choice == 1:
        term = input("Какой термин вы бы хотели перевести с гикского на русский: ")
        if term in geek:
            definition = geek[term]
            print("Ваш термин: ", term, "означает: ", definition)
        else:
            print("Увы. Этот термин мне незнаком")
    elif choice == 2:
        newTerm = input("Введите термин: ")
        if newTerm not in geek:
            newTermDecryption = input("Введите расшифровку термина: ")
            geek[newTerm] = newTermDecryption
            print("Термин добавлен в словарь")
        else:
            print("Такой термин уже есть в словаре")
    elif choice == 3:
        changeTerm = input("Введите термин, толкование которого хотите изменить: ")
        if changeTerm in geek:
            newTermDecryption = input("Введите новую расшифровку термина: ")
            geek[changeTerm] = newTermDecryption
            print("Термин переопределен")
        else:
            print("Возможно вы ошиблись, так как такого термина в словаре нет!")                
    elif choice == 4:
        delTerm = input("Введите термин, который хотите удалить: ")
        if delTerm in geek:
            del geek[delTerm]
            print("Термин удален")
        else:
            print("Возможно вы ошиблись, так как такого термина в словаре нет!")
    else:
        print("Неверный ввод! Попробуйте еще раз")
      
input ("\nНажмите \"Enter\", что бы выйти")
