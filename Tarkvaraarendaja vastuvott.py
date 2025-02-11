from vastuvottDef import *
from random import *

#Ver 0
print("Tere tulemast intervjuule\nMeil on teile mitu küsimust, mis määravad, kas te sobite meile või mitte")
vastus = str(input("Kas alustame: Y/N "))
if vastus.upper() == "Y":
    for i in range(2):  # пока хочу не более 3 вопросов 
        kusim = input(f"{i+1}.{Loe_failist(4)} ")


else:
    print("Nägemiseni")