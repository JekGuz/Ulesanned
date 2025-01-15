import string
from tokenize import Double

# #Ülesanne 1
# vokaalid = ["a","e","u","o","i","ü","ä","ö","õ"]
# konsonanti = "qwrtypsdfghjklzxcvbnm"
# markid = string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# while True:
#     v = k = m = t = 0
#     tekst = input("Sisesta mingi tekst: ").lower()
#     if tekst.isdigit():
#         break
#     else:
#         tekst_list = list(tekst)
#         print(tekst_list)
#         for taht in tekst_list:
#             if taht in vokaalid:
#                 v += 1
#             elif taht in konsonanti:
#                 k += 1
#             elif taht in markid or taht == "ˇ":
#                 m += 1
#             elif taht == " ":
#                 t += 1
#     print("Vokaalid: ", v)
#     print("Konsonanti: ", k)
#     print("Matkid: ", m)
#     print("Tühikud: ", t)

#Ülesanne 2
# # # tuhi_list = [ ]
# # # while True:
# # #     sona = input("Sisesta nimid: ").title
# # #     if sona.isdigit():
# # #         break
# # #     else:

# # #     tuhi_list.append(sona)
# # #     print(tuhi_list)

# #Ülesanne 2
# vanused=[]
# for i in range(7):
#     vanus=int(input(f"{i+1}. Vanus: "))
#     vanused.append(vanus)
# print(f"Sissestage vanused: {vanused}")
# print(max(vanused)) #maksimaalne arv
# print(min(vanused)) #minimaalne arv
# print(sum(vanused)/len(vanused)) # Keskmine arv vanustest

# nimed = []
# for i in range(5):
#     nimi = input(f"{i+1}. Nimi: ")
#     nimed.append(nimi)
# print("Enne sorteerimist: ", nimed)
# nimed.sort()  # Для алфавитного порядка ненужно добавлять ключ
# print("Sorteerimise pärast: ", nimed)
# print("Viimasena lisatud nimi on: ", nimi) #{nimid[4]} {nimid[-1]} {nimi}
# v = input("Kas muudame nimid?: jah/ei ").lower()
# if v == "jah":
#     v = input("Nimi või posotsioon: N/P ").upper()
#     if v == "P":
#         print("Sissesta nimi asukoht: ")
#         v = int(input(" " ))
#         uus_nimi = input("Uus nimi: ")
#         nimed[v-1] = uus_nimi
#     else: 
#         print("Sissesta nimi: ")
#         v = str(input(" " )).title()
#         uus_nimi = input("Uus nimi: ")
#         v = nimed.index(v)
#         nimed[v] = uus_nimi
#     print(nimed)

# #Dublikatit 1
# #dublta = list(set(nimed))
# #print(dublta)

# # # #Dublikatit 2  not work!!!!
# # # d = nimed.count(nimi)
# # # print(f"Dublikatit on {d}")
# # # if d > 1:
# # #     nimed = [name for name in nimed if name != nimi]
# # # else:
# # #     print("Dublikatit ei ole")
# # # print(nimed)

# #Dublikatit 3
# dublta = []
# for nimi in nimed:
#     if nimi not in dublta:
#         dublta.append(nimi)
# print("Mitte korduv loetelu 2. vaariant")
# print(dublta)


# #Ülesanne 3
# värtused = []
# read = int(input("Reade kogus: "))
# for i in range(read):
#     arv = int(input(f"{i+1}. arv: "))
#     värtused.append(arv)
# print(värtused)
# s = input("Sümbol: ")
# for vartus in värtused:
#     print(vartus * s)

#Ülesanne 4
indexID = ["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa", "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"]
print("1 – Tallinn\n2 – Narva, Narva-Jõesuu\n3 – Kohtla-Järve\n4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa\n5 – Tartu linn\n6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa\n7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa\n8 – Pärnumaa\n9 – Läänemaa, Hiiumaa, Saaremaa")
while 1: # while 1 = while True:
    try:
        index = int(input("Sisesta index: "))
        if len(str(index)) == 5:
            break
        else:
            print("On vaja 5 sümnoolid!")
    except:
        print("Vale")
print("index aanalüüs:")
index_list =  list(str(index)) # 1, 2, 3
s1 = int(index_list[0])  # Получаем 1
print(f"Postiindeks {index} on {indexID[s1-1]} ")  #Набор чисел будет идех, во вторых будет Таллинн


