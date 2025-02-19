from random import *

#Ver 1
riik_pealinn = {}  # sõnastik {"Riik":"Pealinn"}

def failist_to_dict(f: str):
    """Laeb riigid ja pealinnad failist sõnastikesse"""
    riik_pealinn = {}  # sõnastik {"Riik":"Pealinn"}
    pealinn_riik = {}  # sõnastik {"Pealinn":"Riik"}
    riigid = []  # järjend, kus talletakse riikide nimetused

    with open(f, 'r', encoding="utf-8-sig") as file:
        for line in file:
            k, v = line.strip().split('-')  # k-võti, v-väärtus
            riik_pealinn[k] = v  # täidame riik_pealinn
            pealinn_riik[v] = k  # täidame pealinn_riik
            riigid.append(k)

    return riik_pealinn, pealinn_riik, riigid

def lisa_faili(failinimi, riik, pealinn):
    """Lisame uus nimi
    Lisame uus nimi
    """
    with open(failinimi, 'a', encoding="utf-8-sig") as file:
        file.write(f"\n{riik}-{pealinn}")

def muuda_faili(failinimi, vriik, uriik, vpealinn, upealinn):
    """Muudame fail
    Kui on vaja muutume riik/pealin
    """
    with open(failinimi, 'r', encoding="utf-8-sig") as file:
        loe_lini = file.readlines()  # Читаем линию полностью

    with open(failinimi, 'w', encoding="utf-8-sig") as file:
        for line in loe_lini:
            if line.strip() == f"{vriik}-{vpealinn}":
                file.write(f"{uriik}-{upealinn}\n") 
            else:
                file.write(line)

    print(f"Vahetasin: {vriik}-{vpealinn} -> {uriik}-{upealinn}")

# Käivitame loodud funktsiooni
riik_pealinn, pealinn_riik, riigid = failist_to_dict("Riigid1.txt")
riigid = list(riik_pealinn.keys())

# List riigid
print(riigid)
print(riik_pealinn.keys())

# List pealinnad
pealinnad = list(riik_pealinn.values())
print(pealinnad)
print(riik_pealinn.values())

# Prindime riikide nimetused
while True:
    sisend = input("Sisesta riigi või pealinna nimi\n'L' lõpetamiseks\n'P' parandamiseks\n'V' Viktoriin\n: ")
    if sisend.upper() == "L":
        break

    # Alustame viktoriin / по могли с вариантом, правда, не знаю надеюсь так подойдет
    elif sisend.upper() == "V":
        print("Viktoriinis on 5 küsimused!")
        hind = 0
        for _ in range(5):
            valik3 = choice(["riik", "pealinn"])
            if valik3 == "riik":
                riik = choice(list(riik_pealinn.keys()))
                vastus = input(f"Mis on {riik} pealinn? ").title()
                if vastus == riik_pealinn[riik]:
                    print("Õige!")
                    hind += 1
                else:
                    print(f"Vale! Õige vastus on {riik_pealinn[riik]}")
            else:
                pealinn = choice(list(pealinn_riik.keys()))
                vastus = input(f"Mis riik on {pealinn} pealinn? ").title()
                if vastus == pealinn_riik[pealinn]:
                    print("Õige!")
                    hind += 1
                else:
                    print(f"Vale! Õige vastus on {pealinn_riik[pealinn]}")
        print(f"Sinu tulemus: {hind}/5 ({round((hind/5)*100, 2)}%)")

    # Lisame veel, kui on midagi vale.
    elif sisend.upper() == "L":  # с заглавной буквой .title()
        vana_riik = input("Sisesta vale riigi nimi (Enter, kui soovid parandada pealinna): ").title()
        vana_pealinn = input("Sisesta vale pealinna nimi (Enter, kui soovid parandada riig): ").title()
        
        # Parandame:

        if vana_riik and vana_riik in riik_pealinn:  # Vaatame, kas on meie vana riik sõnastikust
            uus_riik = input(f"Sisesta uus nimi riigile {vana_riik.upper()}: ").title()
            uus_pealinn = riik_pealinn[vana_riik]  # Pealinn jääb samaks

        elif vana_pealinn and vana_pealinn in pealinn_riik:
            uus_pealinn = input(f"Sisesta uus nimi pealinnale {vana_pealinn.upper()}: ").title()
            uus_riik = pealinn_riik[vana_pealinn]  # Riik jääb samaks
        else:
            print("Sellist riiki või pealinna ei leitud, parandamine pole võimalik.")
            continue

        # Muudame faili ja sõnastikud
        muuda_faili("Riigid1.txt", vana_riik, uus_riik, vana_pealinn, uus_pealinn)
        del riik_pealinn[vana_riik], pealinn_riik[vana_pealinn]
        riik_pealinn[uus_riik] = uus_pealinn
        pealinn_riik[uus_pealinn] = uus_riik

    elif sisend in riik_pealinn:
        print(f"Pealinn: {riik_pealinn[sisend]}")
    elif sisend in pealinn_riik:
        print(f"Riik: {pealinn_riik[sisend]}")
    else:
        print("Sellist riiki või pealinna ei leitud.")
        # Lisame veel riik/pealinn
        ####################### Ei tööta !!!!!!!!!!!!!!!!!!! MIKS?
        valik1 = input("Kas soovid selle lisada? (jah/ei): ").lower()
        if valik1 == "jah":
            valik2 = input(f"Kas '{sisend}' on riik? (jah/ei): ").lower()
            if valik2 == "jah":
                pealinn = input("Sisesta selle riigi pealinn: ").title()
                lisa_faili("Riigid1.txt", sisend, pealinn)  #### Не забывать "" !!! фаил . txt и обязательно в кавычках!!!
                riik_pealinn[sisend] = pealinn  # Lisame sõnastiku
                pealinn_riik[pealinn] = sisend
            else:
                riik = input("Sisesta selle pealinna riik: ").title()
                lisa_faili("Riigid1.txt", riik, sisend)    
                riik_pealinn[riik] = sisend  # Lisame sõnastiku
                pealinn_riik[sisend] = riik
        else:
            print("Alustame uuesti, kui ei soovite lisada")

# Veerud riigid-pealinnad
for key, value in riik_pealinn.items():
    print(key + "-" + value + "\n")



