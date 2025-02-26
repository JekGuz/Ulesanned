from tkinter import *
from PIL import Image, ImageTk
import math
import numpy as np
import matplotlib.pyplot as plt

def lahenda():
    try:
        a = float(tekst_a.get())
        b = float(tekst_b.get())
        c = float(tekst_c.get())

        if a == 0:
            tulemus.config(text="Viga: a ei saa olla 0", bg="red")
            return

        D = b**2 - 4*a*c
        vastus = f"D = {D:.2f}\n"

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            vastus += f"X1 = {x1:.2f}\nX2 = {x2:.2f}"
        elif D == 0:
            x = -b / (2 * a)
            vastus += f"X = {x:.2f}"
        else:
            vastus += "Juur puudub (D < 0)"

        tulemus.config(text=vastus, bg="yellow")

    except:
        tulemus.config(text="Viga: sisestage numbrid!", bg="red")

def joonista():
    try:
        a = float(tekst_a.get())
        b = float(tekst_b.get())
        c = float(tekst_c.get())

        x = np.linspace(-10, 10, 400)
        y = a*x**2 + b*x + c

        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=f"{a}x² + {b}x + {c}", color="blue")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend()
        plt.title("Ruutvõrrandi graafik")
        plt.xlabel("X")
        plt.ylabel("Y")

        plt.show()

    except:
        tulemus.config(text="Viga: sisestage numbrid!", bg="red")

# Создание окна
aken = Tk()
aken.geometry("900x500")
aken.resizable(False, False)
aken.title("Ruutvõrrandi lahendamine")

# Добавляем картинку (фон)
original_pilt = Image.open(r"C:\Users\kotik\source\repos\Ulesanned\ules.jpg")
resize_pilt = original_pilt.resize((900, 500))
bgpilt = ImageTk.PhotoImage(resize_pilt)

labelBg = Label(aken, image=bgpilt)
labelBg.place(x=0, y=0, relwidth=1, relheight=1)  # Размещаем фон по всему окну

# Заголовок
pealkiri = Label(aken, text="Ruutvõrrandi lahendamine", font=("Times New Roman", 24), fg="blue", bg="#c3a4f5", pady=10, width=50)
pealkiri.pack(pady=5)

# Фрейм для коэффициентов
frame_koef = Frame(aken, bg="white")
frame_koef.pack(pady=10)

tekst_a = Entry(frame_koef, font=("Times New Roman", 18), fg="black", bg="white", width=5)
tekst_a.pack(side=LEFT, padx=5)

Label(frame_koef, text="x**2 +", font=("Times New Roman", 18), bg="white").pack(side=LEFT)

tekst_b = Entry(frame_koef, font=("Times New Roman", 18), fg="black", bg="white", width=5)
tekst_b.pack(side=LEFT, padx=5)

Label(frame_koef, text="x +", font=("Times New Roman", 18), bg="white").pack(side=LEFT)

tekst_c = Entry(frame_koef, font=("Times New Roman", 18), fg="black", bg="white", width=5)
tekst_c.pack(side=LEFT, padx=5)

Label(frame_koef, text="= 0", font=("Times New Roman", 18), bg="white").pack(side=LEFT)

# Фрейм для кнопок (кнопки справа от уравнения)
frame_buttons = Frame(aken, bg="white")
frame_buttons.pack(pady=5)

nupp_lahenda = Button(frame_buttons, text="Otsustada", font=("Times New Roman", 18), fg="white", bg="darkgreen", width=15, command=lahenda)
nupp_lahenda.pack(pady=5)

nupp_graafik = Button(frame_buttons, text="Graafik", font=("Times New Roman", 18), fg="white", bg="darkgreen", width=15, command=joonista)
nupp_graafik.pack(pady=5)

# Поле для вывода результата
tulemus = Label(aken, text="", font=("Times New Roman", 18), fg="black", bg="yellow", width=40)
tulemus.pack(pady=10)

aken.mainloop()
