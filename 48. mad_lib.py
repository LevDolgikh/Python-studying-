# Date: 03.08.2021
# Author: Lev Dolgikh

# Сумасшедший сказочник
# Создает рассказ на основе пользовательского ввода

from tkinter import *

class Application(Frame):
    """Основной класс приложения"""
    
    def __init__(self, master):
        """Инициализация класса"""
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        """Создание визуальных элементов"""
        # Инструкция к игре
        Label(self, text = "Введите данные для создания нового рассказа").grid(row =0, column = 0, columnspan = 3, sticky = W)

        # Текстовые поля
        # Текстовое поле "Имя человека"
        Label(self, text = "Имя человека:").grid(row = 1, column = 0, columnspan = 1, sticky = W)
        self.entName = Entry(self)
        self.entName.grid(row =1, column = 2, columnspan = 1, sticky = W)
        # Текстовое поле "Существительное во мн. ч"
        Label(self, text = "Существительное во мн. ч").grid(row =2, column = 0, columnspan = 1, sticky = W)
        self.entNoun = Entry(self)
        self.entNoun.grid(row = 2, column = 2, columnspan = 1, sticky = W)
        # Текстовое поле "Глагол в инфинитиве"
        Label(self, text = "Глагол в инфинитиве").grid(row = 3, column = 0, columnspan = 1, sticky = W)
        self.entVerb = Entry(self)
        self.entVerb.grid(row = 3, column = 2, columnspan = 1, sticky = W)

        # Флажки
        Label(self, text = "Прилагательное(-ые)").grid(row = 4, column = 0, columnspan = 1, sticky = W)
        # Флажок "нетерпиливый"
        self.checkBttn1 = BooleanVar()
        Checkbutton(self, text = "громкий", variable = self.checkBttn1).grid(row = 4, column = 2, columnspan = 1, sticky = W)
        # Флажок "радостный"
        self.checkBttn2 = BooleanVar()
        Checkbutton(self, text = "взбадривающий", variable = self.checkBttn2).grid(row = 4, column = 3, columnspan = 1, sticky = W)
        # Флажок "пронизывающий"
        self.checkBttn3 = BooleanVar()
        Checkbutton(self, text = "пронизывающий", variable = self.checkBttn3).grid(row = 4, column = 4, columnspan = 1, sticky = W)

        # Переключатели
        Label(self, text = "Части тела").grid(row = 5, column = 0, columnspan = 1, sticky = W)
        self.radioBttn = StringVar()
        # Переключатель "рука"
        R1 = Radiobutton(self, text = "рука", variable = self.radioBttn, value = "руку")
        R1.grid(row = 5, column = 2, columnspan = 1, sticky = W)
        # Переключатель "большой палец ноги"
        R2 = Radiobutton(self, text = "большой палец ноги", variable = self.radioBttn, value = "большой палец ноги")
        R2. grid(row = 5, column = 3, columnspan = 1, sticky = W)
        # Переключатель "нога"
        R3 = Radiobutton(self, text = "нога", variable = self.radioBttn, value = "ногу")
        R3.grid(row = 5, column = 4, columnspan = 1, sticky = W)
        # Установить 1 кнопку по умолчанию
        R1.select()

        # Кнопка
        self.bttn = Button(self, text = "Получить рассказ", command = self.generateStory)
        self.bttn.grid(row = 6, column = 0, columnspan = 1, sticky = W)

        # Текстовая область
        self.txt = Text(self, width = 75, height = 100, wrap = WORD)
        self.txt.grid(row = 7, column = 0, columnspan = 5, sticky = W)

    def generateStory(self):
        """Генерирует историю"""
        if self.inputCheck():
            
            # Собирает переменные
            story = ""
            
            name = self.entName.get().title()
            noun = self.entNoun.get().lower()
            verb = self.entVerb.get().lower()
            
            check1 = self.checkBttn1.get()
            check2 = self.checkBttn2.get()
            check2 = self.checkBttn3.get()
            checks = ""
            if check1:
                checks += " громкий"
            if check1:
                checks += " взбадривающий"
            if check1:
                checks += " пронизывающий"
            checks += " крик"

            bodyPart = self.radioBttn.get()

            # Собирает историю
            story += "Обычный человек по имени " + name + " учавствовал(ла) в эксперименте по исследованию темной материи, " \
                    + "вроде все шло по плану, но внезапно раздался гул, вспышка света и, теперь уже отважный герой, перенесся в другой мир." \
                    + " Герой проснулся, так как " + checks + " разбудили его(её). Это были " + noun + ". От страха " + name + " начал(ла) " + verb + ", споткнулся(лась) об " \
                    + bodyPart + " и упал(ла), потеряв сознание, после чего его(её) принесли в жертву местному богу. Мораль - не участвуйте в экспериментах над собой!"

            # Выводит историю в текстовую область
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, story)

    def inputCheck(self):
        """Проверяет заполнены ли поля"""
        allGood = 0
        if self.entName.get() != "" and self.entNoun.get() != "" and self.entVerb.get() != "":
            allGood = 1
        else:
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, "Заполните все поля")
        return allGood
                

class main (object):
    root = Tk()
    root.title("Сумашедший сказочник")
    root.geometry("600x300")
    app = Application(root)
    root.mainloop()
