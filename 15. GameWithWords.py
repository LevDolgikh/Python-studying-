# Date: 01.07.2021
# Author: Lev Dolgikh
import random
# Игра - анаграммы
# Компьютер выбирает какое-пибо слово и хаотически переставляет его буквы
# Задача иrрока - восстановить исходное слово

print ("Добро пожаловать в игру 'Аннаграммы'")
print ("Вам нужно переставить буквы так, что бы получилось осмысленное слово")
print ("Для выхода из программы нажмите 'Enter' не вводя своего слова")

words = ("привет",
         "машина",
         "робот",
         "алгоритм",
         "хочу",
         "найти",
         "работу",
         "возмите",
         "меня",
         "пожалуйста",
         "прошу", )
tryCount = 0
wordsSolved = 0;
yourWord = "ваше слово"
myWord = "загаданное слово"
anagram = ""

while yourWord != "":
    myWord = random.choice(words)
    rightSolution = myWord
    anagram = "";
    while myWord:
        randIndex = random.randrange(len(myWord))
        anagram += myWord[randIndex]
        myWord = myWord[:randIndex]+myWord[randIndex+1:]
    while yourWord != rightSolution and yourWord != "":
        yourWord = input("Анаграмма: " + anagram + ". Введите осмысленное слово из анаграммы! ")
        if yourWord == rightSolution:
            tryCount += 1
            wordsSolved += 1
            print ("Вы угадали c " + str(tryCount) + " попытки!")
        elif yourWord != rightSolution and yourWord != "":
            tryCount += 1
            print ("К сожалению, вы не угадали, попробуйте еще раз!")
print ("\nАнаграмм решено: " + str(wordsSolved) + ". Спасибо за игру!")

input ("\nНажмите \"Enter\", что бы выйти")
