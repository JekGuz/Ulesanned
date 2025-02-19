from tkinter import *
from Graafiline_liides import *


def figuur():
    """
    Vaal ja liplikas
    """
    valik = var.get()
    if valik == 1:
        vaal()
    elif valik == 2:
        liplikas()
    else:
        print("Joonestan hijrm")

# верхний левый угол будет 0.0
aken = Tk()
aken.geometry("900x500")
aken.title("Graafikud")
pealkiri = Label(aken, text = "Erinevad pildid Matplotlib abil", font = "time_new_roman 24", fg = "#0d79de", bg = "#c3a4f5", pady = 20, width = 200)

# Рисуем радио кнопки
var = IntVar()
r1 = Radiobutton(aken, text = "Vaal", font = "time_new_roman 18", variable = var, value = 1, command = figuur)
r2 = Radiobutton(aken, text = "Liplikas", font = "time_new_roman 18", variable = var, value = 2, command = figuur)



pealkiri.pack()
r1.pack()
r2.pack()
aken.mainloop()
