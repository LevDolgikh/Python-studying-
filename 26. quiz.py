# Date: 15.07.2021
# Author: Lev Dolgikh
import sys
# Викторина
# Игра - викторина

def openFile(file_dir = "26. quiz.txt"):
    """Открытие файла для чтения"""
    file = None
    try:
        file = open(file_dir, "r", encoding = 'utf-8')
    except IOError:
        print("Ошибка открытия файла")
        sys.exit()
    return file

def printInstusctions():
    """Вывод инструкций к игре на экран"""
    print("""
        Добро пожаловать в игру 'Викторина'!

        Все просто! Вам задают вопросы - вы на них отвечаете, будте внимательны, только 1 ответ верен.
        Для выхода из игры во время викторины напишите '0'
        """)

def questionsAmount (quizLines):
    quizLen = len(quizLines)
    questionsAmount = 0
    if (quizLen % 9) == 0:
        questionsAmount = quizLen / 9
        print("\nВ текущей викторине ", quizLen / 9, " вопросов")
    else:
        print("Файл викторины не соотвествует требованиям, игра не может быть продолжена")
    return int(questionsAmount)

def theQuestion(quizLines, questionNumber):
    """Обрабатывает 1 вопрос"""
    # Переменные
    questionTopic = ""
    questionItself = ""
    questionText = ""
    answer1 = ""
    answer2 = ""
    answer3 = ""
    answer4 = ""
    rightAnswer = 0
    comment = ""
    playerAnswer = 0

    # Чтение вопроса
    questionBeginning = (questionNumber-1)*9
    questionTopic = quizLines[questionBeginning]
    questionItself = quizLines[questionBeginning+1]
    questionText = quizLines[questionBeginning+2]
    questionText = questionText.replace("/","\n")
    answer1 = quizLines[questionBeginning+3]
    answer2 = quizLines[questionBeginning+4]
    answer3 = quizLines[questionBeginning+5]
    answer4 = quizLines[questionBeginning+6]
    rightAnswer = int(quizLines[questionBeginning+7])
    comment = quizLines[questionBeginning+8]

    # Вывод вопроса, получение ответа, его обработка
    print("\nВопрос номер: ", questionNumber)
    print("Тема вопроса: ", questionTopic)
    print(questionItself)
    print(questionText)
    print("1 - ", answer1, "\n2 - ", answer2, "\n3 - ", answer3, "\n4 - ", answer4) 
    playerAnswer = input("Ваш ответ: ")
    while playerAnswer not in ("0","1","2","3","4"):
        playerAnswer = input("Вы ввели неверное значение, попробуйте снова: ")
    if int(playerAnswer) == rightAnswer:
        print("Это правильный ответ!")
    else:
        print("Увы, вы ответили неправильно, верный ответ: ", rightAnswer)
    print(comment)
    return int(playerAnswer)

def main():
    """Основной код программы"""
    # Переменные
    questionsDone = 0
    playerAnswer = 1
    questions = 0
    
    # Печать инструкций к игре
    printInstusctions()

    # Открытие файла викторины
    fileName = input("Введите имя файла, в котором содержутся вопросы для викторины, \nесли хотите использовать настройки по умолчанию нажмите 'Enter'")
    if fileName != "":
        quizFile = openFile(fileName)
    else:
        quizFile = openFile()

    # Проверка файла викторины и начало игры
    quizLines = quizFile.readlines()
    questions = questionsAmount(quizLines)
    if questionsAmount != 0:
        print("Викторина закружена")
        while questionsDone < questions and playerAnswer != 0:
            playerAnswer = theQuestion(quizLines, questionsDone+1)
            questionsDone += 1
    print("Спасибо за игру, викторина окончена")

    # Выход из программы
    quizFile.close()
    input ("\nНажмите \"Enter\", что бы выйти")
    

main()



