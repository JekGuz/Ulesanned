from random import *

riik_pealinn = {}#sõnastik {"Riik":"Pealinn"}
def failist_to_dict(f:str):
    riik_pealinn = {}#sõnastik {"Riik":"Pealinn"}
    pealinn_riik = {}#sõnastik {"Pealinn":"Riik"}
    riigid = [] #järjend, kus talletakse riigide nimetused
    file=open(f,'r',encoding="utf-8-sig")
    for line in file:
        k,v = line.strip().split('-') #k-võti, v-väärtus
        riik_pealinn[k] = v #täidame riik_pealinn
        pealinn_riik[v] = k #täidame pealinn_riik
        riigid.append(k)
    file.close()
    return riik_pealinn,pealinn_riik,riigid

def lisa_faili(failinimi, riik, pealinn):
    """Lisame uus nimi
    Lisame uus nimi

    """
    with open(failinimi, 'a', encoding="utf-8-sig") as file:
        file.write(f"\n{riik}-{pealinn}")

#käivitame loodud funktsion
riik_pealinn,pealinn_riik,riigid=failist_to_dict("Riigid1.txt")
riigid = list(riik_pealinn.keys())

#list riigid
print(riigid)
print(riik_pealinn.keys())

#list pealinnad
pealinnad = list(riik_pealinn.values())
print(pealinnad)
print(riik_pealinn.values())

#prindime riigide nimetused
while True:
    sisend = input("Sisesta riigi või pealinna nimi (või 'A' lõpetamiseks): ")
    if sisend == "A":
        break
    elif sisend in riik_pealinn:
        print(f"Pealinn: {riik_pealinn[sisend]}")
    elif sisend in pealinn_riik:
        print(f"Riik: {pealinn_riik[sisend]}")
    else:
        print("Sellist riiki või pealinna ei leitud.")
        # Lisame veel riik/pealinn
####################### Ei Töötab !!!!!!!!!!!!!!!!!!! MIKS?
        valik1 = input("Kas soovid selle lisada? (jah/ei): ")
        if valik1.upper() == "JAH":
            valik2 = input(f"Kas '{sisend}' on riik? (jah/ei): ")
            if valik2.upper()  == "JAH":
                pealinn = input("Sisesta selle riigi pealinn: ")
                lisa_faili("Riigid1.txt", sisend, pealinn) #### Не забывать "" !!! фаил . txt и обзательно в ковычках!!!
            else:
                riik = input("Sisesta selle pealinna riik: ")
                lisa_faili("Riigid1.txt", riik, sisend)    
        else:
            print("Alustame uuesti, kui ei soovite lisada")

#Veerud riigid-pealinnad
for key,value in riik_pealinn.items():
    print(key+"-"+value+"\n")



