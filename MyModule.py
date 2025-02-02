from random import *


#Ver 0
loginid = []
paroolid = []
while True:
    print("Kas te olite registrerituud? (Y/N)")
    vasta1 = str(input(": "))
    if vasta1.upper() == "Y":
        while True:
            login = input("Sisesta oma login: ")
            #kontroll listis
            pasw = input("Siseta oma parool: ")
            #kontroll listis
            if login in loginid:
                print("Õige te olite sise logitud!")
                #Vahetamine
                print("Kas soovite vahetada paarol? (Y/N)")
                vastus = str(input(": "))
                if vastus.upper() == "Y":
                    print("Soovite teha tema ise või genererida?")
                    a = str(": ")
                    if a.upper() == "ise":
                        print("Palun kirjutage uus parool")
                        p = str(input(": "))
                        if p.isdigit() and p.isupper():
                            print("Parool soobib!")
                            paroolid.append(p)
                        else:
                            print("Paroolis peab olema tähed ja arved!")
                    if a.upper() == "genererida":
                        str0=".,:;!_*-+()/#¤%&"
                        str1 = '0123456789'
                        str2 = 'qwertyuiopasdfghjklzxcvbnm'
                        str3 = str2.upper()
                        print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
                        str4 = str0 +str1+str2+str3
                        print(str4)
                        ls = list(str4)
                        print(ls)
                        random.shuffle(ls) # type: ignore
                        print(ls)
                        # Извлечь 12 случайных значений из списка
                        psword = ''.join([random.choice(ls) for x in range(12)]) # type: ignore
                        # Пароль готов
                        print(psword)





        else:
            print("Proovi uuesti")

    elif vasta1.upper() == "N":
        print("Soovite registreriida? (Y/N)")
        vasta2 = str(input(": "))

        if vasta2.upper() == "Y":
            login = input("Sisesta oma login: ")
            loginid.append(login)
            pasw = input("Siseta oma parool: ")
            paroolid.append(pasw)
            print("Nüüd te olite registreritud!")
        else:
            print("Nagemiseni!")
            break


