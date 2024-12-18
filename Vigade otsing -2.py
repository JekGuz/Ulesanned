print("*** Arvude mäng ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:  #1 = True
    try:
        a = abs(int(input("Sisesta täisarv => ")))  # abs - натуральное число...
        break
    except ValueError: #  ValueError - тип ошибки
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:
    print("Nulliga on mõttetu töö")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Loendame, mitu on paaris ja mitu paaritu arvu")
    print()
    c = b = a
    paaris = 0
    paaritu = 0

    while b > 0:
        if b % 2 == 0:  #Проверяем четное / нечетное
            paaris += 1
        else:
            paaritu += 1
        b = b // 10 #// откидывает делим оставляя только четное число
    
    print("Paaris:", paaris) #print(f"Paaris: {paaris}")
    print("Paaritu:", paaritu) #print(f"Paaritu: {paaritu}")
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Ümberpöörame* sisestatud arvu")
    print()
    b = 0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*Ümberpöörame* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Tõestame teoreem")
    print()
    # if c % 2 == 0:
    #     print("с - Paaris. jagame 2.")
    # else:
    #     print("с - Paaritu. jagame 3, liidame 1 ja jagame 2.")
    while c != 1:  #!= не равно
        if c % 2 == 0:
            print('{:>4}'.format(round(c))), "- Paaris arv, jagame 2."
            c = c / 2
        else:
            print('{:>4}'.format(round(c)), "- Paaritu arv, korrutame 3, liidame 1 ja jagame 2.")
            c = (3*c + 1) / 2
            # print(c, end="\n")
   
    print('{:>4}'.format(round(c)), "- Teoreem on tõestatud")
    print()