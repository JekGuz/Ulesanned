from tkinter import *
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

global a, b, c, D

# Функция для вычисления корней квадратного уравнения
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
        tulemus.config(text="Viga: sisesta numbrid!", bg="red")

# Функция для построения графика
def joonista():
    try:
        a = float(tekst_a.get())
        b = float(tekst_b.get())
        c = float(tekst_c.get())

        x = np.linspace(-20, 20, 200)
        y = a*x**2 + b*x + c

        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=rf"${a}x^2 + {b}x + {c}$", color="blue")
        plt.axhline(0, color='red', linewidth=0.5)
        plt.axvline(0, color='red', linewidth=0.5)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend()
        plt.title("Ruutvõrrandi graafik")
        plt.xlabel("X")
        plt.ylabel("Y")

        plt.show()
    except:
        tulemus.config(text="Viga: sisesta numbrid!", bg="red")


# # Создание окна
# aken = Tk()
# aken.geometry("900x500")
# aken.resizable(False, False)    # Новое заприщаем расширять окно, как по горизонтале так и по вертикале
# aken.title("Ruutvõrrandi lahendamine")

# # Добаляем картинку (фон)
# original_pilt = Image.open(r"C:\Users\kotik\source\repos\Ulesanned\ules.jpg")
# resize_pilt = original_pilt.resize((900,500))
# bgpilt = ImageTk.PhotoImage(resize_pilt)


# labelBg = Label(aken, image=bgpilt)
# labelBg.place(x=0, y=0)

# # Заголовок
# pealkiri = Label(aken, text="Ruutvõrrandi lahendamine", font="Times_New_Roman 24", fg="#0d79de", bg="#c3a4f5", pady=20, width=100)
# pealkiri.pack()

# # Поля ввода коэффициентов
# tekst_a = Entry(aken, font="Times_New_Roman 18", fg="black", bg="white", width=5)
# tekst_a.pack(side=LEFT, padx=5)

# Label(aken, text="x**2 +", font="Times_New_Roman 18").pack(side=LEFT)

# tekst_b = Entry(aken, font="Times_New_Roman 18", fg="black", bg="white", width=5)
# tekst_b.pack(side=LEFT, padx=5) # padx - отступ

# Label(aken, text="x +", font="Times_New_Roman 18").pack(side=LEFT)

# tekst_c = Entry(aken, font="Times_New_Roman 18", fg="black", bg="white", width=5)
# tekst_c.pack(side=LEFT, padx=5)

# Label(aken, text="= 0", font="Times_New_Roman 18").pack(side=LEFT)

# # Кнопки
# nupp_lahenda = Button(aken, text="Otsustada", font="Times_New_Roman 18", fg="white", bg="darkgreen", width=15, command=lahenda)
# nupp_lahenda.pack(pady=10) #pady - отступ 

# nupp_graafik = Button(aken, text="Graafik", font="Times_New_Roman 18", fg="white", bg="darkgreen", width=15, command=joonista)
# nupp_graafik.pack(pady=10)

# # Поле для вывода результата
# tulemus = Label(aken, text="", font="Times_New_Roman 18", fg="black", bg="yellow", width=40)
# tulemus.pack(pady=20)

# aken.mainloop()

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
labelBg.place(x=0, y=0, relwidth=1, relheight=1)  # Устанавливаем фон

# Создаём контейнер (Frame) для элементов
frame = Frame(aken, bg="#ffffff")
frame.grid(row=0, column=0, columnspan=9, rowspan=9, padx=50, pady=50, sticky="n")

# Заголовок
pealkiri = Label(frame, text="Ruutvõrrandi lahendamine", font=("Times New Roman", 24), fg="blue", bg="#c3a4f5", pady=10)
pealkiri.grid(row=0, column=0, columnspan=6, pady=10)

# Поля ввода коэффициентов
tekst_a = Entry(frame, font=("Times New Roman", 18), fg="black", bg="white", width=5)
tekst_a.grid(row=1, column=0, padx=5)

Label(frame, text="x**2 +", font=("Times New Roman", 18), bg="white").grid(row=1, column=1)

tekst_b = Entry(frame, font=("Times New Roman", 18), fg="black", bg="white", width=5)
tekst_b.grid(row=1, column=2, padx=5)

Label(frame, text="x +", font=("Times New Roman", 18), bg="white").grid(row=1, column=3)

tekst_c = Entry(frame, font=("Times New Roman", 18), fg="black", bg="white", width=5)
tekst_c.grid(row=1, column=4, padx=5)

Label(frame, text="= 0", font=("Times New Roman", 18), bg="white").grid(row=1, column=5)

# Кнопки "Otsustada" и "Graafik"
nupp_lahenda = Button(frame, text="Otsustada", font=("Times New Roman", 18), fg="white", bg="darkgreen", width=15, command=lahenda)
nupp_lahenda.grid(row=1, column=6, padx=10)

nupp_graafik = Button(frame, text="Graafik", font=("Times New Roman", 18), fg="white", bg="darkgreen", width=15, command=joonista)
nupp_graafik.grid(row=1, column=7, padx=10)

# Поле для вывода результата
tulemus = Label(frame, text="", font=("Times New Roman", 18), fg="black", bg="yellow", width=40)
tulemus.grid(row=2, column=0, columnspan=8, pady=20)

aken.mainloop()