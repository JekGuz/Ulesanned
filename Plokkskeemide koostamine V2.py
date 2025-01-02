#0/3. Ülesanne Pärast treeningutega alustamist jooksis sportlane esimesel 
#päeval 10 km. Iga päev suurendas ta oma päevanormi 10% 
#võrra eelmise päeva normist. Kui palju on kogu distants, 
#mille sportlane 7 päeva jooksul läbib?

# v1
km = 10
S = 0
print("Treenigute sportlane")
for i in range(1,8,1):
    km = (km * 0.1) + km
    S = S + km
    print(f"{i} - {round(S, 2)} km")

# v2
i = 1
km = 10
S = 0
while i < 8:
    km = (km * 0.1) + km
    S = S + km
    print(f"{i} - {round(S, 2)}")
    i += 1

# 1. Ülesanne
try:
    n = int(input("Mitu korda me siseneme: "))
    numbers = []

    for i in range(n):
        num = float(input(f"Sisesta {i + 1} number: "))
        numbers.append(num)     #Добавляем число в наш список, который мы добавили и он пустой

    if len(numbers) > 0:  #Проверяем все список наш numbers *len возвращает количество элементов в объекте.
        max = numbers[0]
        for num in numbers:   #Перебираем внутри цикла, все значения в списке numbers
            if num > max:
                max = num
        print("Maksimaalne arv:", max)
    else:
        print("Ei lea numbrid")
except:
    print("Sisesta number")

#Ülesanne 2
try:
    n = int(input("Mitu korda me siseneme: "))
    for i in range(n):
       num = int(input(f"Sisesta {i + 1} number: "))
       if num == 13:
           print("Siseatatud number 77")
       else:
           print(f"Sisestatud number: {num}")
except:
    print("Midagi läks vale")

#Ülesanne 4
while True:
    try:
        tekstiil = float(input("Sisesta kanga pikkus (m): "))
        if tekstiil > 0:
            break
        else:
            print("Kanga pikkus peab olema positiivne arv.")
    except:
        print("Sisesta number")

loik = int(input("Mitu korda me tekstiili lõikame: "))
for i in range(loik):
    if tekstiil <= 0:
        print("Otsas")
        break
    else:
        print(f"Kangas jäänud {round(tekstiil, 2)} m")
    
    try:
        tukk = float(input("Sisestage vajaliku tüki pikkus (m): "))
        if tukk <= 0:
            print("Kanga pikkus peab olema positiivne arv.")
            continue    #Оператор continue в Python используется внутри цикла (for или while) и означает: "Пропустить оставшуюся часть текущей итерации цикла и перейти к следующей итерации".
    except:
        print("Mitte korrektne")
        continue

    if tukk > tekstiil:
        print("Pole piisavalt materjali.")
        choice = input("Kas me ostame kanga? (Jah/ei): ").strip().upper()

        if choice == "JAH":
            print(f"Ülejäänud kangas {round(tekstiil, 2)} m müüdud. Programm on lõpetatud.")
            break
        elif choice == "EI":
            print("Järgmine")
            continue
        else:
            print("Midagi läks valesti, järgmine")
            continue
    else:
        tekstiil -= tukk
        print(f"Lõigatakse ära tükk, mille pikkus on {round(tukk, 2)} m.")

if tekstiil > 0:
    print(f"Programm on lõpetatud. Kangas alles: {round(tekstiil, 2)} m.")



#Ülesanne 5
while True:
    print("Arvutage trapetsi pindala")
    try:
        a = float(input("Sisestage aluse pikkus a: "))
        b = float(input("Sisestage aluse pikkus b: "))
        h = float(input("Sisesta kõrgus h: "))
        if a > 0 and b > 0 and h > 0:
            S = ((a + b) / 2) * h
            print(f"Trapetsi pindala: {S}")
        else:
            print("Midagi läks valesti")
        choice = input("Jätkame (jah/ei): ").strip().upper()
        if choice == "JAH":
             a = float(input("Sisestage aluse pikkus a: "))
             b = float(input("Sisestage aluse pikkus b: "))
             h = float(input("Sisesta kõrgus h: "))
             if a > 0 and b > 0 and h > 0:
                 S = ((a + b) / 2) * h
                 print(f"Trapetsi pindala: {S}")
             else:
                 print("Midagi läks valesti")
        else:
            break
    except:
        print("Sisesta number")

#Ülesanne 6
try:
    n = int(input("Mitu korda me siseneme: "))
    for i in range(n):
        num = int(input("Sisesta number: "))
        if num % 3 == 0:
            print("Väide on õige")
        else:
            print("Väide on vale")
except:
    print("Midagi läks valesti")