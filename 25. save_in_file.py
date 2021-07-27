# Date: 14.07.2021
# Author: Lev Dolgikh
import pickle, shelve
# Запись в файл
# Демонстрирует запись в текстовый файл

# Создание списков
fruits = ["яблоко",
          "банан",
          "груша"]

vegetables = ["картошка",
              "помидорка",
              "оругчик"]

brand = ["Пятерочка",
        "Абрикос",
        "Лама"]

# Запись в файл
print("Консервация списков")
f = open("25. pickles1.dat", "wb")
pickle.dump(fruits, f)
pickle.dump(vegetables, f)
pickle.dump(brand, f)
f.close

# Чтение из файла
print("Чтение списков:")
f = open("25. pickles1.dat", "rb")
fruits = pickle.load(f)
vegetables = pickle.load(f)
brand = pickle.load(f)
print(fruits)
print(vegetables)
print(brand)
f.close

# Чтение с полки
s = shelve.open("25. pickles2.dat")
s["fruits"] = ["яблоко", "банан", "груша"]
s["vegetables"] = ["картошка", "помидорка", "оругчик"]
s["brand"] = ["Пятерочка", "Абрикос", "Лама"]
s.sync()

print("\nИзвлечение списков из файла полки:")
print("фрукты - ", s["fruits"])
print("овощи - ", s["vegetables"])
print("бренды - ", s["brand"])

s.close
input ("\nНажмите \"Enter\", что бы выйти")
