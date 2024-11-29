from calendar import *
from datetime import *
from random import *
from math import *
from tkinter import ROUND


#Ülesanne 1
#paevadekogus = mothrange(2024, 11)[1]
täna = date.today()
tänaf = date.today().strftime("%B %d, %Y")
print(f"Tere! Täna on {tänaf}")
d=täna.day
m=täna.month
y=täna.year
print(d)
print(m)
print(y)
d_l=int(input("Kui palju päevad kuus "))   #kuu_lõpp=int(30-d)
kuu_lõpp=int(d_l - d)
print(f"{kuu_lõpp} on jäänud kuu lõppuni")
#ny = date(2025, 1, 1)
#ny_l = ny - täna
detsP = monthrange(2024, 12)[1] #31
novP = monthrange(2024, 11)[1] #30
jääk1 = detsP + novP
print(f"{jääk1} on aasta lõppuni")

#Ülesanne 2
a = 3+8/(4-2)*2
b = 3+8/4-2*2
c = (3+8)/(4-2)*2
print(a, b, c)

#Ülesanne 3
try:
    r = float(input("Sissesta R: "))
    Sk = pi*r**2
    Lk = 2*pi*r
    Pkv = (2*r)**2
    Lkv = 2*r*4
    print(f"Ruumbe, pimdala on {round(Sk, 2)} \nRingi ümnbermõõt on {round(Lk, 2)} \nRuudu pindala {round(Lkv, 2)} \nRuudu ümbermõtt {round(Lkv, 2)}")
except:
    print("On vaja number!")


#Ülesanne 3i
r=round(random() * 100) #0.0 ... 1.0   int/round
print(r)
Sk = pi*r**2
Lk = 2*pi*r 
Pkv = (2*r)**2 
Lkv = 2*r*4
print(f"Ruumbe, pimdala on {round(Sk, 2)} \nRingi ümnbermõõt on {round(Lk, 2)} \nRuudu pindala {round(Lkv, 2)} \nRuudu ümbermõtt {round(Lkv, 2)}")

#Ülesanne 4
r_maa_km = 6378
euro_sm = 2.575
r_maa_sm = r_maa_km * 100000  #ma*
dlinna_okruznosti = 2 * pi * r_maa_sm
kogus = dlinna_okruznosti / euro_sm
print(f"Maa diametr {round(r_maa_sm, 2)}")
print(f"{round(kogus, 2)} - 2euroseid münte tuleb panna üksteise kõrvale  ")

# #Ülesanne 5
print("kill-koll kill-koll killadi-koll "*4)

#Ülesanne 6 
txt = "Rong see sõitis tsuhh tsuhh tsuhh,\npiilupart oli rongijuht.\nRattad tegid rat tat taa,\nrat tat taa ja tat tat taa.\nAga seal rongi peal,\nkas sa tead, kes olid seal?\n\nRong see sõitis tuut tuut tuut,\npiilupart oli rongijuht.\nRattad tegid kill koll koll,\nkill koll koll ja kill koll kill."
print(txt.upper())  #upper - upper() все символы в верхнем регистре.

#Ülesanne 7
try:
    a = float(input("Palun sisestage ristküliku külg "))
    b = float(input("palun sisestage ristküliku külg "))
    P = 2 * (a + b)
    S = a * b
    print(f"RRistküliku ümbermõõt on {round(P, 2)}, \nRistküliku pindala on {round(S, 2)}")
except:
    print("Peate sisestama numbri!")

#Ülesanne 8 
try:
    kütuse_kogus = float(input("Sisesta tangitud kütuse liitrid "))
    kilomtr = float(input("Sisesta läbitud kilomeetrid "))
    kütusekulu = kütuse_kogus / kilomtr * 100
    km = kütuse_kogus / kilomtr
    print(f"Kütusekulu 100km kohta keskmiselt on {round(kütusekulu, 2)} \nÜhe km maksumus {round(km, 2)}")
except:
    print("Peate sisestama numbri!")

#Ülesanne 9
print("Rulluisutaja keskmine kiirus on 29,9km/h")
V = 29.9
print (f"Möödub minutiga {round(29.9/60, 2)} km")

#Ülesanne 10
try:
    m = int(input("Sisesta aja minutites "))
    h = m // 60
    min = m % 60
    print(f"sisestus {m}, vastus {h}:{min}")
except:
    print("Peate sisestama numri!")