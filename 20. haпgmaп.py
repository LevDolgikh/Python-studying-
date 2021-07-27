# Date: 08.07.2021
# Author: Lev Dolgikh

# Виселица
#
# Классическая игра "Виселица". Компьютер случайным образом выбирает слово
# которое игрок должен отгадать буква за буквой. Если игрок не сумеет
# отгадать за отведенное количество попыток. на экране появится фигурка повешенного.
import random

# Переменные
HANGMAN = (
""" 
------.
|     |
|
|
|
|
|
|
|______
""",
""" 
------.
|     |
|     O
|
|
|
|
|
|______
""",
""" 
------.
|     |
|     O
|    /|\
|
|
|
|
|______
""",
""" 
------.
|     |
|     O
|    /|\

|    |||
|
|
|
|______
""",
""" 
------.
|     |
|     O
|    /|\

|    |||
|     |
|
|
|______
""",
""" 
------.
|     |
|     O
|    /|\

|    |||
|     |
|    | |
|
|______
""",
""" 
------.
|     |
|     O
|    /|\

|    |||
|     |
|    | |
|    | |
|______
""")

MAX_WRONG = len(HANGMAN)-1
WORDS = ("PYTHON","GIVE","ME","THE","JOB","PLEASE")

hiddenWord = []
guessedWord = []
usedChars = []
wrong = 0
randomWord = random.choice(WORDS)

# Определение случайного слова для отгадывания
for char in randomWord:
    hiddenWord.append(char)
    guessedWord.append("-")

# Цикл отгадывания
while wrong < MAX_WRONG and guessedWord != hiddenWord:
    print (HANGMAN[wrong])
    print ("Вы уже отгадали следующие буквы: ", usedChars)
    print ("Отгаданное вами слово выглядит так: ", guessedWord)

    # Ввод буквы
    guessedChar = input("\n\nВведите букву вашу букву: ")

    # Проверка на угадывание
    if guessedChar.upper() in hiddenWord:
        print ("Буква ", guessedChar.upper(), " есть в слове!")

        # заполнение отгаданным символом списков
        usedChars.append(guessedChar.upper())
        i = 0
        for char in hiddenWord:
            if guessedChar.upper() == char.upper():
              guessedWord [i] =  hiddenWord [i]
            i += 1
    #        
    else:
        print ("Буквы ", guessedChar.upper(), " в загаданном слове нет!")
        wrong += 1

# Конец игры
if guessedWord == hiddenWord:
    print ("\n\nПоздравляю! Вы отгадали слово с ", wrong, " ошибок/")
else:
    print ("\n\nУвы, вы проиграли ^(")
    print (HANGMAN[wrong])
   
input ("\nНажмите \"Enter\", что бы выйти")
