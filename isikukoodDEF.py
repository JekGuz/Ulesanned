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
    s = int(str(a[0]))  ### Плохая идея добавить sort - отсортеровал вообще не так как изначально хотела :(
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

# summ1 = s1 * 1 + s2 * 2 + s3 * 3 + s4 * 4 + s5 * 5 + s6 * 6 + s7 * 7 + s8 * 8 + s9 * 9 + s10 * 1
# summ2 = s1 * 3 + s2 * 4 + s3 * 5 + s4 * 6 + s5 * 7 + s6 * 8 + s7 * 9 + s8 * 1 + s9 * 2 + s10 * 3
# jaak1 = summ1 Mod 11
# jaak2 = summ2 Mod 11
# If jaak1 <> "10" Then
# Kontrollnumber = jaak1
# ElseIf jaak1 = "10" Then
# If jaak2 <> "10" Then
# Kontrollnumber = jaak2
# Kontrollnumber = "0"

def kontroll (uk:str)->str:  #mb int
    """ Isikukood kontroll

    :Isikukoodi kontrollnumber formeeritakse „Moodul 11" meetodil, kasutades I või II astme kaalu
    :I astme kaal: 1 2 3 4 5 6 7 8 9 1
    :II astme kaal: 3 4 5 6 7 8 9 1 2 3
    :Näide: isikukoodi 37605030299 kontroll:
    :Summa = 1×3 + 2×7 + 3×6 + 4×0 + 5×5 + 6×0 + 7×3 + 8×0 + 9×2 + 1×9 = 108.
    :108 jääk jagamisel 11-ga on 9. (108/11 ~ 9,8. Täisosa on seega 9. Siit 9*11 = 99. Lahutades 108 – 99 = 9, mis ongi jääk).
    :rtype: str ### mb int
    
    """
    s1 = int(str(uk[0]))
    s2 = int(str(uk[1]))
    s3 = int(str(uk[2]))
    s4 = int(str(uk[3]))
    s5 = int(str(uk[4]))
    s6 = int(str(uk[5]))
    s7 = int(str(uk[6]))
    s8 = int(str(uk[7]))
    s9 = int(str(uk[8]))
    s10 = int(str(uk[9]))
    summ1 = s1 * 1 + s2 * 2 + s3 * 3 + s4 * 4 + s5 * 5 + s6 * 6 + s7 * 7 + s8 * 8 + s9 * 9 + s10 * 1
    summ2 = s1 * 3 + s2 * 4 + s3 * 5 + s4 * 6 + s5 * 7 + s6 * 8 + s7 * 9 + s8 * 1 + s9 * 2 + s10 * 3
    jaak1 = summ1 % 11
    jaak2 = summ2 % 11
    if jaak1 != 10:   
        kontrollnumber = jaak1
    elif jaak2 != 10:
        kontrollnumber = jaak2
    else:
        kontrollnumber = 0 

    return kontrollnumber


