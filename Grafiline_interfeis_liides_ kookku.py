from logging import PlaceHolder
from tkinter import *
from Graafiline_liides import *
global varv

# get получаем инфо, set отдаем инфо
def varvi_valik():
    """

    """
    varv = "white"
    if tekst.get() != "":
        tekst.configure(bg = "yellow")
        varv = tekst.get()
    else:
        tekst.configure(bg = "red")

    return varv

def figuur():
    """
    Vaal ja liplikas
    """
    global varv
    valik = var.get()
    varv = varvi_valik()
    if valik == 1:
        vaal(varv)
    elif valik == 2:
        liplikas(varv)
    else:
        print("Joonestan hijrm")
    return varv

# верхний левый угол будет 0.0
aken = Tk()
aken.geometry("900x500")
aken.title("Graafikud")
pealkiri = Label(aken, text = "Erinevad pildid Matplotlib abil", font = "time_new_roman 24", fg = "#0d79de", bg = "#c3a4f5", pady = 20, width = 200)

# Рисуем радио кнопки
var = IntVar()
r1 = Radiobutton(aken, text = "Vaal", font = "time_new_roman 18", variable = var, value = 1, command = figuur)
r2 = Radiobutton(aken, text = "Liplikas", font = "time_new_roman 18", variable = var, value = 2, command = figuur)

# Создаем тестовый ящик
tekst = Entry(aken, font = "time_new_roman 24", fg = "#0d79de", bg = "#c3a4f5", width = 100)
nupp = Button(aken, text = "Värvi valik", font = "time_new_roman 18", fg = "#0d79de", bg = "#c3a4f5", width = 100, command = varvi_valik)


# Для запуска и распеделения, так же помима pack, place(x = ..., y = ...), grid(column = ..., row = ...)
pealkiri.pack()
tekst.pack()
nupp.pack()
r1.pack()
r2.pack()
aken.mainloop()
