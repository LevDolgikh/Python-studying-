# Date: 29.07.2021
# Author: Lev Dolgikh

# Бесполезные кнопки - 2
# Демонстрирует создание класса в оконном приложении на основе tkinter

from tkinter import *

class Application(Frame):
    """GUI-приложение с тремя кнопками."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        # Первая кнопка
        button1 = Button(self, text = "Я ничего не делаю!")
        button1.grid()
        # Вторая кнопка
        button2 = Button(self)
        button2["text"] = "Я тоже!"
        button2.grid()
        # Третья кнопка
        button3 = Button(self)
        button3.configure(text = "И я!")
        button3.grid()
        

root = Tk()
root.title("Бесполезные кнопки-2")
root.geometry("300x200")

app = Application(root)
app.grid()

root.mainloop()
