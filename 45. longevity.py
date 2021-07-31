# Date: 31.07.2021
# Author: Lev Dolgikh

# Долгожитель
# Демонстрирует текстовое поле. текстовую область и менеджер размещения Grid

from tkinter import *

class Application(Frame):

    def __init__(self, master):
        """Инициализирует рамку"""
        super(Application,self).__init__(master)
        self.grid()
        self.bttnСlicks = 0
        self.createWidget()

    def createWidget(self):
        """Метод для заполнения приложения(рамки)"""
        # Текст инструкций
        self.instLbl = Label(self, text = "Что бы узнать секрет долголетия введите пароль!")
        self.instLbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        # Пометка где писать пароль
        self.pwLbl = Label(self, text = "Пароль:")
        self.pwLbl.grid(row = 1, column = 0, columnspan = 1, sticky = W)
        # Место под пароль
        self.pwEnt = Entry(self)
        self.pwEnt.grid(row = 1, column = 1, columnspan = 1, sticky = W)
        # Кнопка
        self.bttn = Button(self, text = "Узнать секрет", command = self.reveal)
        self.bttn.grid(row = 2, column = 0, columnspan = 1, sticky = W)
        # Текстовая область
        self.txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        """Метод обнавляет счетчик кнопки"""
        contents = self.pwEnt.get()
        message = ""
        if contents == "secret":
            message = "Просто жить? Может повезет..."
        else:
            message = "Не могу поделиться тайной, неверный пароль!"
        self.txt.delete(0.0,END)
        self.txt.insert(0.0,message)

root = Tk()
root.title("Долгожитель")
root.geometry("300x200")
app = Application(root)
root.mainloop()
