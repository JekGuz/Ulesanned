from datetime import *

def kood(xkood:int)->str:
    """ Jagab isikood loendiks

    :koosta igast tähest nimekiri
    :isikukood on int aga tegeme tema str
    :rtype: str
    
    """
    x = list(str(xkood))

    return x

def sugu(a:str)->str:   ### Узнать грамотно ли на каждый иф выводить return 
    """ Määrake inimese sugu esimese numbri järgi

    :Kontrollime võimalikke valikuid läbi if
    :rtype: str
    
    """
    s = int(str(a[0]))
    if s == 1:
        i = print("sugu on mees")
        return i
    elif s == 2:
        i = print("sugu on naine")
        return i
    elif s == 3:
        i = print("sugu on mees")
        return i
    elif s == 4:
        i = print("sugu on naine")
        return i
    elif s == 5:
        i = print("sugu on mees")
        return i
    elif s ==6:
        i = print("sugu on naine")
        return i
    else:
        i = print("ei ole nisugune numberi")
        return i

def sunnipaev(a:str)->date:
    """ Sunnipäev (päev/kuu/aasta)

    :Kuvame isikukoodi abil inimese sünnikuupäeva
    :rtype: date
    
    """



    # sajand = {1: "18", 2: "18", 3: "19", 4: "19", 5: "20", 6: "20"}
     if ikood[0] in number:
            print("Esemene number on: ", ikood[0])   #Чтобы видить результат
            print("Sugu on: ", sugu[ikood[0]])

            aasta = sajand[ikood[0]] + str(ikood[1]) + str(ikood[2])
            kuu = str(ikood[3]) + str(ikood[4])
            paev = str(ikood[5]) + str(ikood[6])
            sunni = f"{aasta}-{kuu}-{paev}"
            print("Sünnipäev: ", sunni)

            try:
                sunni_date = datetime.strptime(sunni, "%Y-%m-%d")
                print("Sünnipäev on korrektne: ", sunni_date.strftime("%d.%m.%Y"))
            except:
                print("Sisestatud isikukoodis sünnipäев pole korrektne!")
