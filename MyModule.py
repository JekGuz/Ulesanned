from random import *
from string import *
from string import punctuation
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from os import path, remove, system
from time import sleep
from os import path, remove, system
from tkinter import simpledialog as sd
from gtts import *
from MyModeleDef import *



# # Запускаем с файлом MyModeleDef --> где def от учителя.

#C:/Users/marina.oleinik/source/repos/Aut_Reg/Salasõnad.txt
salasõnad=loe_failist("salasona.txt")
kasutajanimed=loe_failist("loginid.txt")
while True:
    print(kasutajanimed)
    print(salasõnad)
    
    #räägimine("Tee oma valik", "et")
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine\n")
    vastus=int(input("Sisestage arv: "))
    if vastus == 1:
        print("Registreerimine")
        kasutajanimed,salasõnad = registreerimine(kasutajanimed,salasõnad)
        kirjuta_failisse("loginid.txt", kasutajanimed)
        kirjuta_failisse("salasona.txt", salasõnad)
        saada_kiri(kasutajanimed,salasõnad)

    elif vastus == 2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
        vastus=input("Kas muudame nime, parooli või mõlemad")
        if vastus=="nimi":
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
        elif vastus=="mõlemad":
            print("Nimi muutmine: ")
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
            print("Parooli muutmine: ")
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
    elif vastus==4:
        print("Unustanud parooli taastamine")

    elif vastus==5:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")


# # #Ver 0.5
# salasõnad = loe_failist("Salasõnad.txt")
# kasutajanimed = loe_failist("Kasutajad.txt")
# loginid = [""]
# paroolid = [""]
# while True:
#     print("1. Kas soovite registererida?\n2. Soovite sisselogida\n3. Paarol vahetamine\n4. Kontroll list\n5. Lõpetada")
#     vastus = int(input(": "))
#     # Soovime registerimine
#     if vastus == 1:
#         while True:
#             login = input("Sisesta oma login: ")
#             loginid.append(login)
#     ############# LISAME failid
#             kirjuta_failisse(kasutajanimed, login)
#             print("Teie login salvestatud")
#             break
#         genpsw = input("Soovite ise kirjutada salasõna? (Y/N): ")
#         if genpsw.upper() == "Y":
#             pasw = input("Siseta oma parool: ")
#             paroolid.append(pasw)
#             print("Nüüd te olite registreritud!")
#         if genpsw.upper() == "N":
#             import random
#             str0 =".,:;!_*-+()/#¤%&"
#             str1 = '0123456789'
#             str2 = 'qwertyuiopasdfghjklzxcvbnm'
#             str3 = str2.upper()
#             print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
#             str4 = str0+str1+str2+str3
#             print(str4)
#             ls = list(str4)
#             print(ls)
#             random.shuffle(ls)
#             print(ls)
#             # Извлекаем из списка 12 произвольных значений
#             psword = ''.join([random.choice(ls) for x in range(12)])
#             # Пароль готов
#             paroolid.append(psword)
#             print("Teie uus parool: ", psword)     
#         # Siiseloogime
#     elif vastus == 2:
#         try:
#             login = input("Sisesta oma login: ")
#             pasw = input("Siseta oma parool: ")
#         except:
#             print("Kontrollitud")
#         if login in loginid and pasw in paroolid:
#             print("Õige te olite sise logitud!")
#         else:
#             print("Kontrolli login või parool")
#     # Paarol vahetamine
#     elif vastus == 3:
#         print("Soovite ise kirjutada salasõna? (Y/N)")
#         genpsw = input(": ")

#         if genpsw.upper() == "Y":
#             try:
#                 log = input("Sisesta login: ")
#                 index = loginid.index(log)
#                 logu = input("Siseta uus login: ")
#                 loginid[index] = logu
#             except:
#                 print(f"Teie login: {logu} ")
#             vpsw = input("Sisesta vaana parool: ")
#             index = paroolid.index(vpsw)
#             upsw = input("Siseta uus parool: ")
#             paroolid[index] = upsw
#             print(f"Teie uus parool: {upsw} ")
#         elif genpsw.upper() == "N":
#             try:
#                 log = input("Sisesta login: ")
#                 index = loginid.index(log)
#                 logu = input("Siseta uus login: ")
#                 loginid[index] = logu
#             except:
#                 print(f"Teie login: {logu} ")
#             try:
#                 vpsw = input("Sisesta vana parool: ")
#                 index = paroolid.index(vpsw)
#                 import random
#                 str0=".,:;!_*-+()/#¤%&"
#                 str1 = '0123456789'
#                 str2 = 'qwertyuiopasdfghjklzxcvbnm'
#                 str3 = str2.upper()
#             except:
#                 print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
#             str4 = str0+str1+str2+str3
#             print(str4)
#             ls = list(str4)
#             print(ls)
#             random.shuffle(ls)
#             print(ls)
#             # Извлекаем из списка 12 произвольных значений
#             psword = ''.join([random.choice(ls) for x in range(12)])
#             # Пароль готов
#             paroolid[index] = psword
#             print("Teie uus parool: ", psword)     
#     elif vastus == 4:
#         print("Nimikirjad: ", loginid)
#         print("Salasõnad: ", paroolid)


#     elif vastus == 5:
#         break
        




# # #Ver 0
# loginid = []
# paroolid = []
# while True:
#     print("Kas te olite registrerituud? (Y/N)")
#     vasta1 = str(input(": "))
#     if vasta1.upper() == "Y":
#         while True:
#             login = input("Sisesta oma login: ")
#             #kontroll listis
#             pasw = input("Siseta oma parool: ")
#             #kontroll listis
#             if login in loginid:
#                 print("Õige te olite sise logitud!")
#                 #Vahetamine
#                 print("Kas soovite vahetada paarol? (Y/N)")
#                 vastus = str(input(": "))
#                 if vastus.upper() == "Y":
#                     print("Soovite teha tema ise või genererida?")
#                     a = str(": ")
#                     if a.upper() == "ise":
#                         print("Palun kirjutage uus parool")
#                         p = str(input(": "))
#                         if p.isdigit() and p.isupper():
#                             print("Parool soobib!")
#                             paroolid.append(p)
#                         else:
#                             print("Paroolis peab olema tähed ja arved!")
#                     if a.upper() == "genererida":
#                         str0=".,:;!_*-+()/#¤%&"
#                         str1 = '0123456789'
#                         str2 = 'qwertyuiopasdfghjklzxcvbnm'
#                         str3 = str2.upper()
#                         print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
#                         str4 = str0 +str1+str2+str3
#                         print(str4)
#                         ls = list(str4)
#                         print(ls)
#                         random.shuffle(ls) # type: ignore
#                         print(ls)
#                         # Извлечь 12 случайных значений из списка
#                         psword = ''.join([random.choice(ls) for x in range(12)]) # type: ignore
#                         # Пароль готов
#                         print(psword)

#         else:
#             print("Proovi uuesti")

#     elif vasta1.upper() == "N":
#         print("Soovite registreriida? (Y/N)")
#         vasta2 = str(input(": "))

#         if vasta2.upper() == "Y":
#             login = input("Sisesta oma login: ")
#             loginid.append(login)
#             pasw = input("Siseta oma parool: ")
#             paroolid.append(pasw)
#             print("Nüüd te olite registreritud!")
#         else:
#             print("Nagemiseni!")
#             break

