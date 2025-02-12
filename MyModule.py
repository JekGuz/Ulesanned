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

# #Ver 0.5
# loginid = [""]
# paroolid = [""]
# while True:
#     print("1. Kas soovite registererida?\n2. Soovite sisselogida\n3. Paarol vahetamine\n4. Kontroll list\n5. Lõpetada")
#     vastus = int(input(": "))
#     # Soovime registerimine
#     if vastus == 1:
#         try:
#             login = input("Sisesta oma login: ")
#             loginid.append(login)
#         except:
#             print("Midagi vale")
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


# Работа пренадлежит учителю
def registreerimine(kasutajad:list,paroolid:list)->any:
    """Kirjeldus
    :param list kasutajad: Kirjeldus
    :param list paroolid: Kirjeldus
    :rtype: list,list
    """
    while True:
        nimi=input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool? ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                            flag_p=True
                        elif p in ascii_lowercase:
                            flag_l=True
                        elif p in ascii_uppercase:
                            flag_u=True
                        elif p in digits:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                        räägimine("Sinu kasutajanimi on "+nimi,"et")
                        räägimine("Sinu salasõna on "+parool,"et")
                    break
                else:
                    räägimine("Nõrk salasõna!","et")
                    print("Nõrk salasõna!")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    #mail=sd.askstring("Kirjuta oma e-posti!","Kuhu saada kirja?")
    #email(mail)
    return kasutajad, paroolid
def räägimine(tekst:str,keel:str):
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemast!" kui kasutaja on olemas nimekirjas
        Nimi on järjendis kasutajad
        Salasõna on paroolide järjendis
        Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad:...
    :param list paroolid:...
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")              
        if nimi in kasutajad:            
            while True:
                parool=input("Sisesta salasõna: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print(f"Tere tulemast! {nimi}")
                        break                   
                except:
                    print("Vale nimi või salasõna!")
                    if p==5: 
                        print("Proovi uuesti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek")
        else:
            print("Kasutajat pole")
def nimi_või_parooli_muurmine(list_:list):
    """
    """
    muutuja=input("Vana nimi või parool: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uus nimi või parool: ")
        list_[indeks]=muutuja
    return list_
def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,'r',encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def kirjuta_failisse(fail:str,järjend=[]):
    """Salvestame tekst failisse
    """
    #n=int(input("Mitu: "))
    #for i in range(n):
    #    järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,'w',encoding="utf-8")
    for element in järjend:
        f.write(element+"\n")
    f.close()
def ümber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,'a')
    text=input("Sisesta tekst:")
    f.write(text+"\n")
    f.close()
def failide_kustutamine():
    """
    """
    failinimi=input("Mis fail tahad eemaldada?") #path.isdir("Kaust")
    if path.isfile(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} oli kustutatud")
    else:
        print(f"Fail {failinimi} puudub")
def loe_ankeet(fail:str)->any:
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    #kus_vas={}
    for line in fail:
        n=line.find(":")# , - разделитель
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())
    
        #k,v=line.strip().split(":")
        #kus_vas[k]=v
        
    fail.close()
    return kus,vas #,kus_vas