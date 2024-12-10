from datetime import *
from math import *

#Ülesanne 1
nimi = input("Mis on sinu nimi? ")
if nimi.upper() == "JUUKU":
    print("Lähme kinno")
else:
    print("Ootan Juuku")

nimi = input("Mis on sinu nimi? ")
if nimi.isalpha() and nimi.isupper():
    if nimi == "JUUKU":
        print("Lähme kinno")
        try:
            vanus = int(input(f"Kui vana sa oled {nimi}? "))
            if vanus < 0:
                print("Viga!")
            elif vanus <= 6:
                print("Tasuta")
            elif vanus < 15:
                print("Lastepilet")
            elif vanus < 65: 
                print("Täispilet")
            elif vanus < 100:
                print("Sooduspilet")
            else:
                print("Nii palju!!!")
        except:
            print("Täesarv oli vaja sisestada")
    else:
        print("Ootan Juuku")
else:
    print("Segatud sõna")

#Ülesanne 2
nimi1 = input("1. Mis sinu nimi on? ")
nimi2 = input("2. Mis sinu nimu on? ")
nimed = ["Katja","Ravil","Ksenia"]
if nimi1.isalpha() and nimi2.isalpha():
    if (nimi1 in nimed) and (nimi2 in nimed):
        print("Nad on pinginabrid")
    else:
        print("Nad on ei ole naabrid")
else:
    print("Viga!")

#Ülesanne 2.i teine vaariant
nimi1 = input("1. Mis sinu nimi on? ")
nimi2 = input("2. Mis sinu nimu on? ")
nimed = ["Katja","Ravil","Ksenia"]
if nimi1 == "Katja" and nimi2 == "Ravil" or nimi1 == "Ravil" and nimi2 == "Katja" :
    print("Nad on pinginabrid")
else:
    print("Nad on ei ole naabrid")

#Ülesanne 3
try:
    a = float(input("Pikkus: "))
    b = float(input("Laius: "))
    S = a * b
    print(f"Põranda pindala {S} m**2")
    vastus = input("Kas tahad remondi teha?(Jah-1/ei-0) ") #Ждем ответ "JAH" ).upper тогде проще условия
    if vastus.upper()=="JAH" or vastus == "1":
        print("Reemont")
        hind = float(input("Ühe meetri hind: "))
        summa = S * hind
        print(f"Remoondi kuulud: {summa} eur")
    elif vastus.upper()=="EI" or vastus == "0":
        print("-")
    else:
        print("Ei saa aru!")
except:
    print("Numbrid!!!")

#Ülesanne 4
try:
    hind = float(input("Missugune sinu hind? "))
    if hind >= 700:
        summa = hind - (hind * 0.3)
        print(f"Soodustusega hinna: {round(summa, 2)} eur")
    else:
        print(f"Tavalina hind: {hind} eur")
except:
    print("Numberid!")

#Ülesanne 5
try:
    t = float(input("Mis on toas temperatuur? "))
    if t >= 18:
        print(f"Teie toa temperatuur {t} soobib talvel")
    else:
        print(f"Teie toa temperatuur {t} ei soobi talvel")
except:
    print("Viga temperatuur")

#Ülesanne 6
try:
    h = float(input("Mis on sinu pikkus? "))
    if h >= 45 and h <= 150:
        print("Teie pikkust peetakse madalaks")
    elif h > 150 and h <= 180:
        print("Teie pikkust peetakse keskmiseks")
    elif h > 180 and h <= 230:
        print("Teie pikkust peetakse kõrgeks")
    else:
        print("Kindel")
except:
    print("Viga pikkus")

# Ülesanne 7 сначала один пол потом другой
try:
    sugu = input("Kas sa oled naine (N) või mees (M)? ")
    if sugu.upper() == "N":
        h = float(input("Kui pikk sa oled? "))
        if h <= 100:      #h < 45 and h > 150:
            print("Sina oled madala kasvu")
        elif h <= 175: #h < 150 and h > 175:
            print("Sina oled keskmist kasvu")
        elif  h <= 200: #h < 175 and h > 200:
            print("Sina oled pikka kasvu")
        else:
            print("Kas sa oled kindel? ")
    elif sugu.upper() == "M":
        h = float(input("Kui pikk sa oled? "))
        if h <= 160:  #h < 50 and h > 160:
            print("Sina oled madala kasvu")
        elif h  <= 180:  #h < 160 and h > 185:
            print("Sina oled keskmist kasvu")
        elif h <= 220:  #h < 185 and h > 220:
            print("Sina oled pikka kasvu")
        else:
            print("Kas sa oled kindel? ")
    else:
        print("Sisesta õigesti: Kas N või M ")
except:
    print("Viga")

Ülesanne 8 
# # try:
# #     leib = input("Kas te tahate osta leib (Y/N)? ")
# #     if leib.upper() == "Y":
# #         leibtk = int(input("Kui palju: "))
# #         pimm = input("Kas te tahate osta pimm (Y/N)? ")
# #         if pimm.upper() == "Y":
# #             pimmtk = int(input("Kui palju: "))
# #             vorst = input("Kas te tahate osta vorst (Y/N)? ")
# #             if vorst.upper() == "Y":
# #                 vorsttk = int(input("Kui palju: "))
# #                 just = input("Kas te tahate osta just (Y/N)? ")  
# #                 if just.upper() == "Y":
# #                     justtk = int(input("Kui palju: "))
# #     else:
# #         pimm = input("Kas te tahate osta pimm (Y/N)? ")
# #         if pimm.upper() == "Y":
# #             pimmtk = int(input("Kui palju: "))
# #             vorst = input("Kas te tahate osta vorst (Y/N)? ")
# #             if vorst.upper() == "Y":
# #                 vorsttk = int(input("Kui palju: "))
# #                 just = input("Kas te tahate osta just (Y/N)? ")  
# #                 if just.upper() == "Y":
# #                     justtk = int(input("Kui palju: "))
# #         else:
# #             vorst = input("Kas te tahate osta vorst (Y/N)? ")
# #             if vorst.upper() == "Y":
# #                 vorsttk = int(input("Kui palju: "))
# #                 just = input("Kas te tahate osta just (Y/N)? ")  
# #                 if just.upper() == "Y":
# #                     justtk = int(input("Kui palju: "))
# #             else:
# #                 just = input("Kas te tahate osta just (Y/N)? ")  
# #                 if just.upper() == "Y":
# #                     justtk = int(input("Kui palju: "))
                
# # except:
# #     print("Viga")

###Ülesanne 8.1
# # try:
# #     list = ["leib", "pimm", "vorst", "juust", "kana", "kala", "banaan"]
# #     print(f"Tooded laos:\n{list[0]};\n{list[1]};\n{list[2]};\n{list[3]};\n{list[4]};\n{list[5]};\n{list[6]};")
# #     valik = input("Palun kirjuta misugune toote soovite oosta: ")
# #     if list in ["leib", "pimm", "vorst", "juust", "kana", "kala", "banaan"]:
# #         valitudtoote = list[int(valik) -1]
# #         kogus = int(input(f"Kogus valitud {valitudtoote}: "))
# #         if kogus.isdigit() and int(kogus) > 0:
# #             print(f"Teie valik oli: {valitudtoote} ja tema kogus: {kogus}")
# #         else:
# #             print("Vale kogus!")
    
       
# # except:
# #     print("viga!")

#Ülesanne 9
try:
    a = float(input("Sisesta ruudu külja: "))
    b = float(input("Sisesta ruudu külja: "))
    if a == b:
        S = a * b
        print(f"See on ruut ja selle S on võrdne {round(S, 2)}")
    else:
        print("See ei ole ruut")
except:
    print("Palun kirjuta numbrid!")

#Ülesanne 10
try:
    a = float(input("Sisesta esimene arv: "))
    b = float(input("Sisesta teine arv: "))
    tehet = input("Sisesta tehet + - * /: ")
    if tehet == "+":
        s = a + b
        print(f" a + b = {s}")
    elif tehet == "-":
        s = a - b
        print(f" a - b = {s}")
    elif tehet == "*":
        s = a * b
        print(f" a * b = {s}")
    elif tehet == "/":
        s = a / b
        print(f" a / b = {s}")
    else:
        print("midagi läks viga!")   
except:
    print("Palun kirjuta numbrid!")

#Ülesanne 11
try:
    sün = input("Sisesta oma sünnipäeva YYYY-MM-DD: ")
    sünp = datetime.strptime(sün, "%Y-%m-%d")
    tana = datetime.today()
    aasta = tana.year - sünp.year
    if aasta > 0 and aasta %10 == 0:
        print("Sul on juubel")
    else:
        print("Sul ei ole juube")
except:
    print("Midagi läks viga!")

#Ülesanne 12
try:
    a = float(input("Sisesta toote hind: "))
    if a <= 10:
        summa = a - (a * 0.1)
        print(f"soodushind on võrdne {summa}")
    elif a > 10:
        summa = a - (a * 0.2)
        print(f"soodushind on võrdne {summa}")
    else:
        print("Ei saa aru see hind!")
except:
    print("Midagi läks viga!")

#Ülesanne 13
try:
    sugu = input("Missugune sugu teil  on(M/N)? ")
    if sugu.upper() == "M":
        sün = input("Sisesta oma sünnipäeva YYYY-MM-DD: ")
        sünp = datetime.strptime(sün, "%Y-%m-%d")
        tana = datetime.today()
        aasta = tana.year - sünp.year
        if aasta >= 16 and aasta <= 18:
            print("Ootame jalgpalli meeskonda")
        else:
            print("Ootame 16 - 18 poisid!")
    else:
        print("Meil on vaja meest.")
except:
    print("Ootame meest!")

Ülesanne 14
try:
    print("Tere tulemas!\nMeie firma pakub 20-kohalisi bussid")
    arv = int(input("Kui palju teil on inimesed? "))
    summa = arv / 20
    jääk = arv % 20
    if jääk == 0:
        print(f"Teil on vaja {round(summa)} bussi;\nKõik bussid on täis!")
    else:
        print(f"Teil on vaja {ceil(summa)} bussi;\nViimases bussis {jääk} inimest")
except:
    print("Viga!")