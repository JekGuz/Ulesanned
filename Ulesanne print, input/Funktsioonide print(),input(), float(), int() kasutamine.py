from random import *  #* - все функции, второй вариант, если обращаемся к определенной функции, randint as rd 
from math import * # матаматические функции, в данный момент Пи

# Ülesanne 1
print("Tere maailm!")
nimi=input("Palun kirjuta oma nimi ").capitalize()   #lower() - все маленькие, upper() - все большие, capitalize() - первая будет всегда большая другие маленькие
print("Tere tulemast! Tervitan sind " + nimi + "!")
print("Tere tulemast! Tervitan sind" , nimi + "!")   #"," действует как " " а затем идет слова "+" обьядиняет тобишь Слова если до не было пробела будет написано слитно
try:   #try если будет ошибка не будет выдавать до except
    vanus=int(input("Kui vana sa oled? "))
    print("Tere Tulemast! Tervitan sind" , nimi , "Sa oled", vanus , "aastat vana.")
    print(f"\tTere Tulemast! Tervitan sind  {nimi} Sa oled {vanus} aastat vana.")
    except:
        print("On vaja numbrid sissestada!")


# Ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käeb_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))

# Ülesanne 3  import имя_модуля или from имя_модуля import *
kokku=randint(1,1000)
print(f"Kokku on {kokku} kommi")
kommi=int(input("Mittu kommi sa tahad? "))
kokku = kokku - kommi
print(f"Jääk on {kokku} kommi")

#Ülesanne 4  L=2*P*R d=L/P
print("Läbimõõdu leidmine ")
#l - ümbermõõt
l=float(input("Ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")

#Ülesanne 5
print("Hakkame lugeda ristkülikukujulise maatüki diagonaal")
N=float(input("Palun sisesta ristküliku pikkus N "))
M=float(input("Palun sisesta ristküliku laius M "))
d=sqrt(N**2 + M**2)   #** - используемым для возведения в степень
print(f"Ristkülikukujulise maatüki diagonaal on {round(d,2)}")

# Ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))  #забыли поздаровоться 
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg    #На оборот надо делить
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#Ülesanne 7
print ("Aritmeetilise keskmine")
a = float(input("1. "))
b = float(input("2. "))
c = float(input("3. "))
d = float(input("4. "))
e = float(input("5. "))
keskmine = (a+b+c+d+e)/5
print(f"Aritmeetilise keskmine on {keskmine}")


# Ülesanne 8  
print("     @..@")
print("    (----)")
print("  ( | __ | )")
print("   ^^    ^^")

#Ülesanne 9
print ("Arvutame kolmnurga ümbermõõdu")
a = float(input("a "))
b = float(input("b "))
c = float(input("c "))
P = a+b+c
print (f" Kolmnurga ümbermõõdu {P}")

#Ülesanne 10
P=int(input("Mitu inimest käes resto? "))
h=float(input("Mitu eurot maksab pitsa? "))
joot_raha=float(input("Mitu % jootraha? "))
pitsa_joot = h*(1+joot_raha/100)
iga_üks=pitsa_joot/P
print(f"Iga üks maksab {round(iga_üks,2)}")
