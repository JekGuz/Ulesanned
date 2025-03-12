from tkinter import *
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


# Создаем два словаря с буквами и значения из таблицы
def loo_vene_tabel():
    """
    Vene Table
    """
    return {
        'А': 1, 
        'Б': 2, 
        'В': 3, 
        'Г': 4, 
        'Д': 5, 
        'Е': 6, 
        'Ё': 7, 
        'Ж': 8, 
        'З': 9,
        'И': 1, 
        'Й': 2, 
        'К': 3, 
        'Л': 4, 
        'М': 5, 
        'Н': 6, 
        'О': 7, 
        'П': 8, 
        'Р': 9,
        'С': 1, 
        'Т': 2, 
        'У': 3, 
        'Ф': 4, 
        'Х': 5, 
        'Ц': 6, 
        'Ч': 7, 
        'Ш': 8, 
        'Щ': 9,
        'Ъ': 1, 
        'Ы': 2, 
        'Ь': 3, 
        'Э': 4, 
        'Ю': 5, 
        'Я': 6
    }

def loo_ladina_tabel():
    """
    Eesti tabel
    """
    return {
        'A': 1, 
        'B': 2, 
        'C': 3, 
        'D': 4, 
        'E': 5, 
        'F': 6, 
        'G': 7, 
        'H': 8, 
        'I': 9,
        'J': 1, 
        'K': 2, 
        'L': 3, 
        'M': 4, 
        'N': 5, 
        'O': 6, 
        'P': 7, 
        'Q': 8, 
        'R': 9,
        'S': 1, 
        'T': 2, 
        'U': 3, 
        'V': 4, 
        'W': 5, 
        'X': 6, 
        'Y': 7, 
        'Z': 8
    }

# Какому словарю будут принадлежать все буквы /
def tuvasta_tähestik(nimi):
    """
    Kontrollime tahed
    """
    ru_tähed = set("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    eng_tähed = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

    nimi_tähed = set(nimi)  # Имя делит на каждую букву, чтобы ВСЕ проверить

    # мы проверяем, все ли буквы имени входят в русский или латинский алфавит спомощью issubset все ли входят буквы в весь словарь
    if nimi_tähed.issubset(ru_tähed): 
        return 'ru'
    elif nimi_tähed.issubset(eng_tähed):
        return 'eng'
    else:
        return None  # Из разных алфавитов

# Считаем буквы, делаем их верхними точно все, и находим в словаре arvuta_nime_number + reduktsioon
def arvuta_nime_number(nimi, tabel):
    """
    1 Arvestamine
    """
    nimi = nimi.upper()
    summa = sum(tabel.get(täht, 0) for täht in nimi if täht in tabel)
    return (summa - 1) % 9 + 1    # - нашла формулу, сама не додумалась! 

# Функция для сохранения результата в файл
def salvesta_tulemus(nimi, number):
    """
    Faili salvestamine
    """
    with open("nimetulemused.txt", "a", encoding="utf-8") as file:
        file.write(f"{nimi}: {number}\n")

def arvuta():
    nimi = sisend.get().strip()
    tähestik = tuvasta_tähestik(nimi)
    if tähestik == 'ru':
        tabel = loo_vene_tabel()
    elif tähestik == 'eng':
        tabel = loo_ladina_tabel()
    else:
        messagebox.showerror("Viga", "Kontroll nimi")
        return
    
    # Вычисляем число имени
    number = arvuta_nime_number(nimi, tabel)
    # Загружаем словарь с описаниями чисел из файла
    number_tahendus = failiavamine(r"C:\Users\kotik\source\repos\Ulesanned\Textnum.txt")
    # Получаем значение из файла, если есть, иначе пишем "Tähendus puudub"
    tahendus = number_tahendus.get(f"*{number}", "Tähendus puudub")
    # Обновляем Label tulemus: показываем число и его объяснение
    tulemus.config(text=f"{number}\n{tahendus}")

    return number



# Функция для сохранения результата
def salvesta():
    nimi = sisend.get().strip()
    if nimi:
        number = arvuta()
        if number:
            salvesta_tulemus(nimi, number)
            messagebox.showinfo("Salvestatud", "Salvestatud")
    else:
        messagebox.showwarning("Hoiatus", "Hoiatus")

# Фаил открытие - взяла у Анны  
def failiavamine(fail):
    global number_tahendus
    number_tahendus = {}

    with open(fail, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()  # Убираем пробелы и переносы строк

            if not line or '-' not in line:  # Пропускаем пустые строки и строки без "-"
                print({line})
                continue
            
            parts = line.split('-', 1)  # Разделяем строку по первому "-"
            
            if len(parts) == 2:  # Проверяем, что получилось два элемента
                k, v = parts
                number_tahendus[k.strip()] = v.strip()  # Убираем лишние пробелы

    return number_tahendus

# Делаем открытие для октрытия файла -  взяла у Анный

# Создание графического интерфейса
aken = Tk()
aken.title("Nime numbri arvutaja")
aken.geometry("500x500")

original_pilt = Image.open(r"C:\Users\kotik\source\repos\Ulesanned\numbers.jpg")
resize_pilt = original_pilt.resize((500, 500))
bgpilt = ImageTk.PhotoImage(resize_pilt)

# Устанавливаем фон
labelBg = Label(aken, image=bgpilt)
labelBg.place(x=0, y=0, relwidth=1, relheight=1) 


# Окна добаляем
Label(aken, text="Numegoloogia!", font=("Monotype Corsiva", 25),bg="SystemButtonFace", padx=30).grid(row=0, column=0)

# Окна добаляем
Label(aken, text="Sisesta nimi:", font=("Monotype Corsiva", 18), fg="black", bg="SystemButtonFace", padx=30).grid(row=2, column=0)
sisend = Entry(aken, font=("Monotype Corsiva", 18), fg="black", bg="#e7b2a4", width=27)  # #e7b2a4 - розовое золото
sisend.grid(row=3, column=0, padx=40)

# Метка для вывода результата   / В две строчке иначе не считывается tulemus - что находиться в расчетах (arvesta)
Label(aken, text="Teie number:", font=("Monotype Corsiva", 18), fg="black", bg="SystemButtonFace", padx=30).grid(row=5, column=0)
# # tulemus = Text(aken, font=("Monotype Corsiva", 12),fg="black",bg="#e7b2a4", height=5, width=40, wrap=WORD)
# # tulemus.grid(row=6, column=0)
tulemus = Label(aken, font=("Monotype Corsiva", 18), text="", fg="black",bg="#e7b2a4", padx=30)
tulemus.grid(row=6, column=0)

# Кнопки
Button(text="Arvuta number", font=("Monotype Corsiva", 18), fg="black", bg="SystemButtonFace", command=arvuta).grid(row=4, column=0)
Button(text="Salvesta tulemus", font=("Monotype Corsiva", 18), fg="black", bg="SystemButtonFace", command=salvesta).grid(row=7, column=0)


# Запуск интерфейса
aken.mainloop()




