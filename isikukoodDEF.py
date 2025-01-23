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

def sunnipaev(a:str)->str:  ### -> date не работала коректно ( узнать )
    """ Sunnipäev (päev/kuu/aasta)

    :Kuvame isikukoodi abil inimese sünnikuupäeva
    :rtype: date
    
    """

    esemene = int(str(a[0]))
    if esemene == 1 or esemene == 2:
        sajand = "18"
        aasta = sajand + str(a[1]) + str(a[2])
        kuu = str(a[3]) + str(a[4])
        paev = str(a[5]) + str(a[6])
        sunni = f"{aasta}-{kuu}-{paev}"
        try:
            sunni_date = datetime.strptime(sunni, "%Y-%m-%d")
            return sunni_date.strftime("%d.%m.%Y")
        except:
            return "Sisestatud isikukoodis sünnipäеv pole korrektne!"


    elif esemene == 3 or esemene == 4:
        sajand = "19"
        aasta = sajand + str(a[1]) + str(a[2])
        kuu = str(a[3]) + str(a[4])
        paev = str(a[5]) + str(a[6])
        sunni = f"{aasta}-{kuu}-{paev}"
        try:
            sunni_date = datetime.strptime(sunni, "%Y-%m-%d")
            return sunni_date.strftime("%d.%m.%Y")
        except:
            return "Sisestatud isikukoodis sünnipäеv pole korrektne!"

    elif esemene == 5 or esemene == 6:
        sajand = "20"
        aasta = sajand + str(a[1]) + str(a[2])
        kuu = str(a[3]) + str(a[4])
        paev = str(a[5]) + str(a[6])
        sunni = f"{aasta}-{kuu}-{paev}"
        try:
            sunni_date = datetime.strptime(sunni, "%Y-%m-%d")
            return sunni_date.strftime("%d.%m.%Y")
        except:
            return "Sisestatud isikukoodis sünnipäеv pole korrektne!"




