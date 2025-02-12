from random import *
def failist_to_dict(f:str):
    riik_paelinn = {} # sõnastik {"Riik": "Pealinn"}
    pealinn_riik = {} # Sõnastik {"Pealinn": "Riik"}
    riigid1 = [] #järjend, kus talletakse riigide nimitused
    file = open(f, 'r', encoding ="utf-8-sig")
    for line in file:
        k, v = line.strip().split('-') #k-võti, v - väärtus
        riik_paelinn[k] = v #täidame riik_pealinn
        pealinn_riik[v] = k #täidame pealinn_riik
        riigid1.append(k)
        file.close()
        return riik_paelinn,pealinn_riik,riigid1

#käivitamine loodud funktsion
riik_pealinn, pealinn_riik, riigid1 = failist_to_dict("Riigid1.txt")
riigid = list(riik_pealinn.keys())

#list pealinnad
print(riigid)
print(riik_pealinn.keys())

pealinnad = list(riik_pealinn.values())

#list riigide nimetused
print(pealinnad)
print(riik_pealinn.values())

#prindimi riigide nimetusd
while True:
    riik = input("Riik: ")
    if riik == "A": break
    print("Pealinn: ", riik_pealinn[riik])

#Veerud riigid-pealinnad
for key, value in riik_pealinn.items():
    print(key+"-"+value+"\n")


from random import *

def failist_to_dict(f: str):
    riik_paelinn = {}
    pealinn_riik = {}
    riigid = []

    with open(f, 'r', encoding="utf-8-sig") as file:
        for line in file:
            k, v = line.strip().split('-')
            riik_paelinn[k] = v
            pealinn_riik[v] = k
            riigid.append(k)

    return riik_paelinn, pealinn_riik, riigid

# käivitamine loodud funktsion
riik_pealinn, pealinn_riik, riigid = failist_to_dict("Riigid1.txt")

# list pealinnad
print("Riigid:", list(riik_pealinn.keys()))

# list riigide nimetused
pealinnad = list(riik_pealinn.values())
print("Pealinnad:", pealinnad)

# prindimi riigide nimetusd
while True:
    riik = input("Riik: ")
    if riik == "A": break
    print("Pealinn:", riik_pealinn.get(riik, "Sellist riiki pole nimekirjas!"))

# Вывод всех пар "страна - столица"
for key, value in riik_pealinn.items():
    print(f"{key} - {value}")

