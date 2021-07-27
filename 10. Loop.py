# Date: 30.06.2021
# Author: Lev Dolgikh

# Петля
# Демонстрирует работу с циклом for и оператором range()

word = input ("Введите слово")

print ("Вот все буквы вашего слова по порядку")
for letter in word:
    print(letter)

print ("С 1 до 10 по порядку")
for i in range (10):
    print(i, end=" ")

print ("\nС 0 до до 50 кратные 5")
for i in range (0, 50, 5):
    print(i, end=" ")

print ("\nС 10 до до 0 в обратном порядке")
for i in range (10, 0, -1):
    print(i, end=" ")
    
input ("\nНажмите \"Enter\", что бы выйти")
