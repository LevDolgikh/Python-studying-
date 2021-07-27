# Date: 05.07.2021
# Author: Lev Dolgikh

# Арсенал героя 3.0
# Демонстрирует работу со списками

# Пустой кортеж
inventory = ["меч",
             "кольчуга",
             "щит",
             "целебное снадобье"]

if not inventory:
    print ("Вы безоружны")

print ("\nСодержимое кортежа:")
print (inventory)

print ("\nСодержимое вашего инвентаря:")
for item in inventory:
    print (item)

print ("\nВы нашли книгу")
book = ["загадочкая книга"]
inventory += book

print ("\nСодержимое инвертаря:")
print (inventory)

print ("\nВы поменяли меч на арбалет")
inventory[0] = "арбалет"

print ("\nСодержимое инвертаря:")
print (inventory)

print("Зa золото и драгоценные камни: вы купили магический кристалл. способный предсказывать будущее.")
inventory[1:3] = ["магический кристалл"]
print("Teпepь в вашем распоряжении:")
print (inventory[0])
print (inventory[1])
print (inventory[2])
print (inventory[3])
del inventory[3]

input ("\nНажмите \"Enter\", что бы выйти")
