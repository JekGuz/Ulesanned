from datetime import *
from math import *

#Ülesanne 1
try:
    a = int(input("Sisesta number: "))
    if a > 0:
        print("Positiivne")
        if int(a) % 2 == 0:
            print("Paarisarv")
        else:
            print("paaritu arv")
    else:
        print("Negatiivne")
except:
    print("Midagi läks viga!")

#Ülesanne 2
try:
    a = int(input("Sisesta number: "))
    b = int(input("Sisesta number: "))
    c = int(input("Sisesta number: "))
    if a > 0 and b > 0 and c > 0:
        nurk = a+b+c==180
        print(f"Võivad olla ühe kolmnurga nurgad {nurk}")
        if a==b==c:
            print("See on võrdkülgne kolmnurk")
        elif a==b or b==c or c==a:
            print("See on võrdhaarne kolmnurk")
        else:
            print("See on isekülgne kolmnurk")
    else:
        print(f"Võivad olla ühe kolmnurga nurgad {nurk}")
except:
    print("Midagi läks viga!")

#Ülesanne 3
try:
    sugu = input("Kas sa oled naine (M) või mees (N)? ")
    if sugu.upper() == "M":
        list = ["esmaspäev", "teisipäev", "kolmapäev", "neljapäev", "reedel", "laupäev", "pühapäev"]
        print(f"nädalapäevad:\n0. {list[0]};\n1. {list[1]};\n2. {list[2]};\n3. {list[3]};\n4. {list[4]};\n5. {list[5]};\n6. {list[6]};")
        p = int(input("Sisesta number: "))
        if p < len(list):   #len провереям в списке, спасибо exel
            print(f"See on {list[p]}")
        else:
            print("Sisestatud number ei vasta nädalapäevade indeksile (0-6).")
    else:
        print("Head päeva!")


except:
    print("Midagi läks viga!")

#Ülesanne 4
#zodiac = [("Kaljukits", (22, 12), (19, 1)), ("Veevalaja", (20, 1), (18, 2)), ("Kalad", (19, 2), (20, 3) )), ("Jäär", (21, 3), (19, 4)), ("Sõnn", (20, 4), (20, 5)), ("Kaksikud", (21, 5), (20, 6)), ("Vähk", (21, 6), (22, 7)), ("Lõvi", (23, 7), (22, 8)), ("Neitsi" , (23, 8), (22, 9)), ("Kaalud", (23, 9), (22, 10)), ("Skorpion", (23, 10), (21, 11)), ("Ambur", (22, 11), (21, 12)), ("Kaljukits", (22, 12), (31, 12))]
try:
    p = int(input("Sisesta sünnipäeva kuupäev (1-31): "))
    k = int(input("Sisesta sünnipäeva kuu (1-12): "))
    if (21 <= p <= 31 and k == 1) or (1 <= p <= 19 and k == 2):
        print("Sina oled Veevalaja")
    elif (20 <= p <= 29 and k == 2) or (1 <= p <= 20 and k == 3):
        print("Sina oled Kala")
    elif (21 <= p <= 31 and k == 3) or (1 <= p <= 20 and k == 4):
        print("Sina oled Jäär")
    elif (21 <= p <= 30 and k == 4) or (1 <= p <= 21 and k == 5):
        print("Sina oled Sõnn")
    elif (22 <= p <= 31 and k == 5) or (1 <= p <= 21 and k == 6):
        print("Sina oled Kaksikud")
    elif (22 <= p <= 30 and k == 6) or (1 <= p <= 22 and k == 7):
        print("Sina oled Vähk")
    elif (23 <= p <= 31 and k == 7) or (1 <= p <= 23 and k == 8):
        print("Sina oled Lõvi")
    elif (24 <= p <= 31 and k == 8) or (1 <= p <= 23 and k == 9):
        print("Sina oled Neitsi")
    elif (24 <= p <= 30 and k == 9) or (1 <= p <= 23 and k == 10):
        print("Sina oled Kaalud")
    elif (24 <= p <= 31 and k == 10) or (1 <= p <= 22 and k == 11):
        print("Sina oled Skorpion")
    elif (23 <= p <= 30 and k == 11) or (1 <= p <= 21 and k == 12):
        print("Sina oled Ambur")
    elif (22 <= p <= 31 and k == 12) or (1 <= p <= 20 and k == 1):
        print("Sina oled Kaljukits")
    else:
        print("Sisesta õiged andmed")
except:
    print("Midagi läks viga!")

#Ülesanne 5
a = input("Sisesta arv või text: ")
try:
    n = float(a)  # Преобразуем в число (целое или дробное)
    if n.is_integer():  # Если число целое
        summa = n * 0.5
        print(f"Sisestasite täisarvu. 50% {n} = {summa}")
    else:
        summa = n * 0.7
        print(f"Sisestasite täisarvu. 70% {n} = {round(summa, 2)}")
except:
    if a.isalpha():  # Если текст состоит только из букв
        print(f"Te sisestasite text: {a}")
    else:
        print("Midagi läks viga!")

#Ülesanne 6
try:
    y = input("Kas lahendame tasandamise?(Y/N) ")
    if y.upper() == "Y":
        a = float(input("Sisesta number: "))
        b = float(input("Sisesta number: "))
        c = float(input("Sisesta number: "))
        D = (b**2) - (4 * a * c)
        if D > 0:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            print(f"Võrrandis on kaks vastust: {round(x1, 2)} ja {round(x2, 2)}")
        elif D == 0:
            x = -b / (2 * a)
            print(f"Võrrandis on üks vastust: {round(x, 2)}")
        elif D < 0:
            print("Lahendusi pole")
        else:
            print("Load...")
    else:
        print("Head päeva!")

except:
    print("Midagi läks viga!")