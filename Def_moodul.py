from math import *

def summa3(arv1:int, arv2:int, arv3:int)->int:  ### целые числа арв1, 2, 3 и целые получу 
    """ Tagastab kolme täisarvu summa

    :param int arv1: Esimene number
    :param int arv2: Teine number
    :param int arv3: Kolmas number
    :rtype: int
    
    """
    summa = arv1 + arv2 + arv3
    return summa

def arithmetic(arv1:float, arv2:float, op:str) -> int:
    """Lihtsamad aritmeetilised tehted

    :Kirjutage aritmeetiline funktsioon, millel on 3 argumenti: 
    :esimesed 2 on arvud, kolmas on tehe, mis tuleks nendega sooritada. 
    :Kui kolmas argument on +, lisa need; kui -, siis lahuta; * - korrutada; / - jaga. 
    :Muudel juhtudel tagastage string "Tundmatu toiming".
    :rtype: float

    """
    ##operatsionid = ["+", "-", "/", "*"]
    if op == "+":
        summa = arv1 + arv2
    elif op == "-":
        summa = arv1 - arv2
    elif op == "/":
        summa = arv1 / arv2
    elif op == "*":
        summa = arv1 * arv2
    else:
        print("Vale sisendus")
    return summa


def arithmetic2(a:float, b:float, t:str) -> any:
    """Lihtsamad aritmeetilised tehted

    :Kirjutage aritmeetiline funktsioon, millel on 3 argumenti: 
    :esimesed 2 on arvud, kolmas on tehe, mis tuleks nendega sooritada. 
    :Kui kolmas argument on +, lisa need; kui -, siis lahuta; * - korrutada; / - jaga. 
    :Muudel juhtudel tagastage string "Tundmatu toiming".
    :rtype: float or str

    """
    if t in ["+", "-", "*", "/"]:
        if b ==0 and t == "/":
            vastus = "DIV/0"
        else:
            vastus = eval(str(a) + t + str(b))
    else:
        vastus = "Tundmatu teha"

    return vastus

def is_year_leap (a:int)->bool: #bool - True / False выдает значение
    """ Liigaaasta

    :Kirjutage funktsioon on_aasta_hüpe, 
    :mis võtab 1 argumendi - aasta ja tagastab Tõene, 
    :kui aasta on liigaasta, ja False muul juhul.
    :rtype: float and str

    """
    if a % 4 == 0:   # Делится на 4, делится на 100
        a = True
    else:
        a = False
    return a

def square (a:float)->str:
    """ Ruut

    :Kirjutage funktsiooni ruut, mis võtab 1 argumendi - ruudu 
    :külje ja tagastab 3 väärtust: ruudu ümbermõõt, 
    :ruudu pindala ja ruudu diagonaal.
    :rtype: str

    """
    P = a * 4
    S = a ** 2
    d = a * sqrt(2) # **1/2 не выдавало точного значения d = (2)**(1/2)*a

    return (f"S: {S}, P: {P}, d: {round(d,2)}")

def season (k:int)->str:
    """ Aastaajad
    :Kirjutage aastaaja funktsioon, mis võtab ühe argumendi - 
    :kuu numbri (1 kuni 12) ja tagastab hooaja, kuhu see kuu kuulub 
    :(talv, kevad, suvi või sügis).
    :rtype: str

    """
    # if k < 1 or k > 12:
    #     return ("Vale number")

    # hooajal = {
    # "talv": [12, 1, 2],
    # "kevad": [3, 4, 5],
    # "suvi": [6, 7, 8],
    # "sügis": [9, 10, 11]
    # }

    # for vastu, kuud in hooajal.items():
    #     if k in kuud:
    #         return (f"Praegu on selline hooaeg: {vastu}")

    if 1 <= k <=12:
        if k in [1,2,12]: 
           vastu = "Winter"
        elif k in [3, 4, 5]: 
           vastu = "Spring"
        elif k in [3, 4, 5]:
           vastu = "Summer"
        elif k in [9, 10, 11]: 
           vastu = "Autumm"
        else: 
           vastu = "System error"
        return vastu


def bank(years: int, a: float)->float:
     """ Bank
    :Kasutaja teeb euro sissemakse perioodiks 10% aastas 
    :(iga aastaga suureneb tema hoiuse suurus 10%. 
    :See raha lisatakse hoiuse summale ja järgmisel aastal lisandub sellele ka intress ).
    :rtype: float

    """
     #S = a * (1+0.1)**years
     S = a * ((1 + 0.1)**years)
     
     return round(S, 2)