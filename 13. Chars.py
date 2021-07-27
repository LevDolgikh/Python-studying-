# Date: 30.06.2021
# Author: Lev Dolgikh

# Символ
# Демонстрирует. как создавать новые строки из исходных с помощью цикла for

print ("Здравстуйте! У моего хорошего товарища, аглоритма рекурсии, сегодня день рождения: ", \
       "если хотите, то можите его поздравить, но... Он не любит гласные, поэтому я обработаю ", \
       "ваш текст перед его передачи алгоритму рекурсии.")
congratulation = input ("\nВведите текст:")

consonants = "бвгджзйклмнпрстфхцчшщ!?., "
processedCongratulation = ""

for char in congratulation:
    if char in consonants or char.upper() in congratulation:
        processedCongratulation += char

print ("Вот какое сообщение я передал рекурсии: ", processedCongratulation[:], \
       "\nОн очень рад, передал вам следующие: Спсб!")
        
input ("\nНажмите \"Enter\", что бы выйти")
