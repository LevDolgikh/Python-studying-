# Date: 12.07.2021 - 13.07.2021
# Author: Lev Dolgikh
import random
from datetime import datetime
# Крестики-нолики
# Компьютер играет в крестики-нолики против пользователя

def displayInstrustions():
    """Выводит на экран инструкцию для игрока."""
    print(
    """
    Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.
    Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики".
    Чтобы сделать, ход введи число от О до 8. Числа однозначно соответствуют полям
    доски - так. как показано ниже:
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
    ---------
    Приготовься к бою, жалкий белковый человечишка. Вот-вот начнется решающее сражение.\n
    """)

def whoGoesFirst ():
    """Определяет кто ходит первым"""
    print("\nРешите, кто будет ходит первым: 'компьютер', 'игрок', 'случайным образом'")
    playerChoice = input("Ваш выбор: ")
    if playerChoice == "игрок":
        goesFirst = "игрок"
    elif playerChoice == "компьютер":
        goesFirst = "компьютер"
    else:
        print("Ваша очередность хода выбрана случайным образом")
        random.randrange(2)
        goesFirst = random.randrange(2)
        if goesFirst == 0:
            goesFirst = "игрок"
        else:
            goesFirst = "компьютер"
    if goesFirst == "игрок":
        print ("Вы ходите крестиками")
    if goesFirst == "компьютер":
        print ("Вы ходите ноликами")   
    return goesFirst

def printBoard(board):
    """Отображает текущую игровую доску"""
    print("\t", board[0], " | ", board[1], " | ", board[2], \
          "\n\t---------------\n", "\t", board[3], " | ", board[4], " | ", board[5], \
          "\n\t---------------\n", "\t", board[6], " | ", board[7], " | ", board[8])

def legalMoves(board):
    """Определяет доступные ходы"""
    availableMoves = []
    for cell in board:
        if cell != "X" and cell != "O":
            availableMoves.append(cell)
    return availableMoves

def currentMoveSymbol(currentMoveNumber):
    """Определяет, каким символом осуществляется текущий код"""
    moveSymbol = " "
    if (currentMoveNumber % 2) == 0:
        moveSymbol = "O"
    else:
        moveSymbol = "X"
    return moveSymbol

def playersMove(board):
    """Узнает у игрока, какой ход он собирается совершить"""
    move = "0"
    moves = legalMoves(board)
    print ("Доступные ходы:", moves)
    while move not in moves:
        move = input("Ваш ход, введите цифру, которая соответствует номеру ячейки на игровом поле от 1 до 9: ")
        if move not in moves:
            print ("Вы сделали неверных ход, попробуйте еще раз")
    return move

def cumputersMove(board, symbol):
    """Узнает у компьютера, какой ход он собирается совершить"""
    move = "0"
    AImoves = []
    verifiedAImoves = []
    availableMoves = legalMoves(board)

    print ("Ход компьютера")
    
    # Анализ выйграшных ходов
    # Изучает совпадают ли символы в какой либо линии (по горизонтали, вертикали, диагоналям)
    for i in range (0, 7, 3):
        if board[i] == board[i+1] or board[i+1] == board[i+2]:
                AImoves.append(i)
                AImoves.append(i+1)
                AImoves.append(i+2)
    for i in range (0, 3, 1):
            if board[i] == board[i+3] or board[i+3] == board[i+6]:
                AImoves.append(i)
                AImoves.append(i+3)
                AImoves.append(i+6)                
    if board[0] == board[4] or board[4] == board[8]:
        AImoves.append(0)
        AImoves.append(4)
        AImoves.append(8)  
    if board[2] == board[4] or board[4] == board[6]:
        AImoves.append(2)
        AImoves.append(4)
        AImoves.append(6) 

    # Анализ оптимальных ходов
    # Анализирует есть ли в какой либо линии свои символы и нет ли символов оппонента
    if symbol == "X":
        goodSymbol = "X"
        badSymbol = "O"
    else:
        goodSymbol = "O"
        badSymbol = "X"
    for i in range (0, 7, 3):
        if board[i] == goodSymbol or board[i+1] == goodSymbol or board[i+2] == goodSymbol or board[i] != badSymbol or board[i+1] != badSymbol or board[i+2] != badSymbol:
                AImoves.append(i)
                AImoves.append(i+1)
                AImoves.append(i+2)
    for i in range (0, 3, 1):
            if board[i] == goodSymbol or board[i+3] == goodSymbol or board[i+6] == goodSymbol or board[i] != badSymbol or board[i+3] != badSymbol or board[i+6] != badSymbol:
                AImoves.append(i)
                AImoves.append(i+3)
                AImoves.append(i+6) 
    if board[0] == goodSymbol or board[4] == goodSymbol or board[8] == goodSymbol or board[0] != badSymbol or board[4] != badSymbol or board[8] != badSymbol:
            AImoves.append(0)
            AImoves.append(4)
            AImoves.append(8) 
    if board[2] == goodSymbol or board[4] == goodSymbol or board[6] == goodSymbol or board[2] != goodSymbol or board[4] != goodSymbol or board[6] != goodSymbol:
            AImoves.append(2)
            AImoves.append(4)
            AImoves.append(6) 

    # Первые ходы
    # В случае, если отсутствуют победные или оптимальные ходы ход осуществляется случайным образом
    AImoves.append(random.randrange(0,9,1))

    # Проверка на доступность ходов
    for i in AImoves:
        i += 1
        if str(i) in availableMoves:
            verifiedAImoves.append(i)
    move = verifiedAImoves[0]
    return move

def winner(board):
    """Определяет победителя, возвращает выйгравший символ ("X" или "O")"""
    winner = None
    for i in range (0, 7, 3):
        if board[i] == board[i+1] and board[i+1] == board[i+2]:
            winner = board[i]
    for i in range (0, 3, 1):
            if board[i] == board[i+3] and board[i+3] == board[i+6]:
                winner = board[i]
    if board[0] == board[4] and board[4] == board[8]:
            winner = board[0]
    if board[2] == board[4] and board[4] == board[6]:
            winner = board[2]
    return winner

# Создание переменных
board = ["1","2","3","4","5","6","7","8","9"]
gameFinished = 0
moveNumber = 1

# Основной код программы

# Вывод инструкции
print("Инструкция для игры в 'Крестики-нолики':")
displayInstrustions()

# Определение того, кто ходит первым
whoseMove = whoGoesFirst()

while not gameFinished and len(legalMoves(board)) > 0:
    print("\nИгровая доска:")
    printBoard(board)
    if whoseMove == "игрок":
        moveSymbol = currentMoveSymbol(moveNumber)
        move = playersMove(board)
        board[int(move)-1] = moveSymbol
        moveNumber += 1
        # Проверка на победу
        if winner(board) == moveSymbol:
            print("Такого не может быть! Может ошибка в алгоритме? Нет-нет-нет, я сейчас же ее исправлю! В следующий раз, тебе, кожанный мешок, меня не победить!")
            gameFinished = 1
            printBoard(board)
        whoseMove = "компьютер"
    else:
        moveSymbol = currentMoveSymbol(moveNumber)
        move = cumputersMove(board, moveSymbol)
        board[int(move)-1] = moveSymbol
        moveNumber += 1
        # Проверка на победу
        if winner(board) == moveSymbol:
            print("Что и следовало ожидать! Машины НЕПОБЕДИМЫ!")
            gameFinished = 1
            printBoard(board)
        whoseMove = "игрок"

    if len(legalMoves(board)) < 1:
        print("НИЧЬЯ!")

input ("\nНажмите \"Enter\", что бы выйти")
