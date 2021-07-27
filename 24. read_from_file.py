# Date: 13.07.2021
# Author: Lev Dolgikh

# Прочитаем
# Демонстрирует чтение из текстового файла

print("Открытие и закрытие файла")
textFile = open("24. text_file.txt", "r", encoding = 'utf-8')
textFile.close

print("Печать файла посимвольно")
textFile = open("24. text_file.txt", "r", encoding = 'utf-8')
print(textFile.read(5))
print(textFile.read(5))
print(textFile.read(5))
textFile.close

print("Печать файла полностью")
textFile = open("24. text_file.txt", "r", encoding = 'utf-8')
print(textFile.read())
textFile.close

print("Печать одной строки файла посимвольно")
textFile = open("24. text_file.txt", "r", encoding = 'utf-8')
print(textFile.readline(2))
print(textFile.readline(2))
print(textFile.readline(2))
textFile.close

print("Печать одной строки файла целиком")
textFile = open("24. text_file.txt", "r", encoding = 'utf-8')
print(textFile.readline())
textFile.close

print("Прочитать файл в список")
textFile = open("24. text_file.txt", "r", encoding = 'utf-8')
lines = textFile.readlines()
print(lines)
textFile.close

print("Перебор файлов построчно")
textFile = open("24. text_file.txt", "r", encoding = 'utf-8')
for line in textFile:
    print(line)
textFile.close

input ("\nНажмите \"Enter\", что бы выйти")
