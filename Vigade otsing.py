from math import *  #import * from math не правильный порядок

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #float это число может быть любое
S= a ** 2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)  #было написано '' вместо "
di=a * sqrt(2) # убрала math и оставила не sqr, а sqrt
print("Ruudu diagonaal", round(di,2))
print() #пустая строка?
print("Ristküliku karakteristikud") #лишния )
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #float это число может быть любое
c=float(input("Sisesta ristküliku 2. külje pikkus => "))  #float это число может быть любое
S=b*c
print("Ristküliku pindala", S) #Не хватает ""
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
di=sqrt((b**2)+(c**2)) # d di=math.sqrt(b*2+c*2) убрала math и самой формуле ** добавила
print("Ristküliku diagonaal", round(di, 2)) #Нехватало round( , 2)
print()  #пустая строка?
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #"" не правильные, не хватало float( это число может быть любое
d=2*r #* между 2r нужно поставить действия (оператора) *
print(f"Ringi läbimõõt {d}")   #запись не верная
S=pi*(r**2) # Pi без (), ** в квадрате 
print("Ringi pindala", round(S, 2)) # round(что, сколько после , )
C=2*pi*r # Pi без (), * не хватало
print("Ringjoone pikkus", round(C, 2)) # ) не хватает, round(что, сколько после , )
