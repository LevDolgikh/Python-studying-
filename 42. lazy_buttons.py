# Date: 29.07.2021
# Author: Lev Dolgikh

# Бесполезные кнопки
# Демонстрирует создание кнопок

from tkinter import *

root = Tk()
root.title("Бесполезные кнопки")
root.geometry("300x200")

app = Frame(root)
app.grid()
button1 = Button(app, text = "Я ничего не делаю!")
button1.grid()
button2 = Button(app)
button2["text"] = "Я тоже!"
button2.grid()
button3 = Button(app)
button3.configure(text = "И я!")
button3.grid()
root.mainloop()
