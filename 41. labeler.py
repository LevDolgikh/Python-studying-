# Date: 29.07.2021
# Author: Lev Dolgikh

# Это я. метка
# Демонстрирует применение меток

from tkinter import *

root = Tk()
root.title("Использование меток")
root.geometry("300x200")

app = Frame(root)
app.grid()
lbl = Label(app, text = "Вот она я")
lbl.grid()
root.mainloop()
