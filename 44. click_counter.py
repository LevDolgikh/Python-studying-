# Date: 31.07.2021
# Author: Lev Dolgikh

# Счетчик щелчков
# Демонстрирует связывание событий с обработчиками

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
        self.bttn1 = Button(self)
        self.bttn1["text"] = "Количество щелчков 0"
        self.bttn1["command"] = self.updateCount
        self.bttn1.grid()

    def updateCount(self):
        """Метод обнавляет счетчик кнопки"""
        self.bttnСlicks += 1
        self.bttn1["text"] = "Количество щелчков: " + str(self.bttnСlicks)
        
        

root = Tk()
root.title("Счетчик щелчков")
root.geometry("300x200")
app = Application(root)
root.mainloop()
