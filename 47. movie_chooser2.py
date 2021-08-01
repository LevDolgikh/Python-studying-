# Date: 01.08.2021
# Author: Lev Dolgikh

# Киноман
# Демонстрирует применение флажков

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
        self.label1 = Label(self, text = "Укажите ваши любымые жанры кино")
        self.label1.grid(row = 0, column = 0, sticky = W)
        self.label2 = Label(self, text = "Выберите все, что вам по вкусу:")
        self.label2.grid(row = 1, column = 0, sticky = W)
        # Переключатели
        self.favorite = StringVar()
        self.favorite.set(None)
        # Флажки
        # флажок "Комедия"
        Radiobutton(self,
                    text = "Комедия",
                    variable = self.favorite,
                    value = "комедии.",
                    command = self.updateText
                    ).grid(row = 2, column = 0, sticky = W)
        # флажок "Драма"
        Radiobutton(self,
                    text = "Драма",
                    variable = self.favorite,
                    value = "драмы.",
                    command = self.updateText
                    ).grid(row = 3, column = 0, sticky = W)
        # флажок "Романтика"
        Radiobutton(self,
                    text = "Романтика",
                    variable = self.favorite,
                    value = "романтика.",
                    command = self.updateText
                    ).grid(row = 4, column = 0, sticky = W)
        # Тестовая область
        self.txt = Text(self,width = 40, height = 5, wrap = WORD)
        self.txt.grid(row = 5, column = 0, columnspan = 3, sticky = W)
        

    def updateText(self):
        """Обновляется по мере тогоЮ как пользователь выбирает свои любимые жанры"""
        likes = ""
        likes += "Вам нравятся " + self.favorite.get()
        self.txt.delete(0.0,END)
        self.txt.insert(0.0,likes)

root = Tk()
root.title("Флажки")
root.geometry("300x200")
app = Application(root)
root.mainloop()
