# Date: 30.06.2021
# Author: Lev Dolgikh

# Длина
# Демонстрирует работу функции len() и оператора in

word = input ("Введите текст")

print ("\nДлина введенного вами текста составляет: " + str(len(word)) + " символа" )


print ("Всем известно, что наиболее часто употребляемая согласная в русском языке это  - 'н'", \
end=" ")

if "н" in word:
    print ("и она также встречается и в вашем тексте!")
else:
    print ("но в вашем тексте она не встречается...Странно, очень странно...")
    
input ("\nНажмите \"Enter\", что бы выйти")
