# Date: 14.07.2021
# Author: Lev Dolgikh
import pickle, shelve
# Исключения
# Демонстрирует обработку исключительных ситуаций

# try/exept
try:
    num = float(input("Введите число: "))
except:
    print("Похоже это не число")

try:
    num = float(input("Введите число: "))
except ValueError:
    print("Похоже это не число")

try:
    num = float(input("Введите число: "))
except ValueError:
    print("Похоже это не число")
else:
    print("Вы ввели число:", num)
                
input ("\nНажмите \"Enter\", что бы выйти")
