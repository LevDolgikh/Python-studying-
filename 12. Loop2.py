# Date: 30.06.2021
# Author: Lev Dolgikh
import random
# Петля 2
# Демонстрирует индексацию строк и доступ к символам

word = "индекс"

print ("\nВ переменной word храниться слово: " + word + "\n")
high = len(word)
low = -len(word)
for i in range (10):
    position = random.randrange (low, high)
    print ("word[", position, "]\t" , word[position])
        
input ("\nНажмите \"Enter\", что бы выйти")
