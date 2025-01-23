
from datetime import *
from isikukoodDEF import *

###VER 1
ikoodid = []
arvud = []
while True:
    print("Kas soovite kontrollida isikukood? (Y/N)")  ### По совету учителя выйти из цикла с вопросом ( Добавила еще один иф)
    vastu = str(input(": "))
    if vastu.upper() == "Y":
        try:
            isik = int(input("Sisesta isukukood: "))
        except:
            print("Vaja arv")
            continue

        if len(str(isik)) == 11:
            print("Isikukood on õige")
            ikoodid.append(isik)
            ikoodid.sort() 

            ### Будем разбирать цифру с помощью def
            ikood = kood(isik)
            print(ikood)

            ### Определяем пол человека по первый цифры через def (без библиотеки буду делать через 6 иф)
            sugu = sugu(ikood) ### обратилась к списку в самой функции def там у меня [0] - первое число списка ikood

            ### Дата рождения p.s без словаря опять через иф 


        else:
            print("Isikukood on vale")
            arvud.append(isik)
            arvud.sort() 

        print("Praegu listis meil on:")
        print("Isikukoodid: ", ikoodid)
        print("Arvud: ", arvud)
    else:
        print("Nägemeseni!")
        break


# ##VER 0
# ikoodid = []
# sugu = {
#  1: "mees",
#  2: "naine",
#  3: "mees",
#  4: "naine",
#  5: "mees",
#  6: "naine",
#     }
# arvud = []
# number = [1, 2, 3, 4, 5, 6]
# sajand = {1: "18", 2: "18", 3: "19", 4: "19", 5: "20", 6: "20"}
# arv = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]  ### список для контроля исикукода
# sunnitusmaja = {
# range(1, 11): "Kuressaare haigla", ### Это стандартный способ в Python создать последовательность чисел от 1 до 10 включительно (верхняя граница 11 не включается).
# range(11, 20): "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla",
# range(21, 221): "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)",
# range(221, 271): "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla",
# range(371, 421): "Narva Haigla",
# range(421, 471): "Pärnu Haigla",
# range(471, 491): "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla",
# range(491, 521): "Järvamaa Haigla (Paide)",
# range(521, 571): "Rakvere, Tapa haigla",
# range(571, 601): "Valga Haigla",
# range(601, 651): "Viljandi Haigla",
# range(651, 700):  "Lõuna-Eesti Haigla (Võru), Põlva Haigla"  
#     }
# while True:
#     try:
#         isik = int(input("Sisesta isukukood: "))
#     except:
#         print("Vaja arv")
#         continue  

#     if len(str(isik)) == 11:
#         print("Isikukood on õige")
#         ikoodid.append(isik)
#         ikoodid.sort() 

#         ### разбиваем красиво искукод в каждую цифру
#         ikood = list(map(int,str(isik)))  #Результатом работы map является новый объект, содержащий преобразованные элементы.
#         print(f"Isikukood: {ikood}")  #Чтобы видить результат
       
#        ### Выясняем пол
#         # # s = int(str(ikood[0]))
#         # # print("Sugu number on: ", sugu[s])  делала после потом увидила что я уже вычислила первую букву

#         ### Вычисляем пол / дату
#         if ikood[0] in number:
#             print("Esemene number on: ", ikood[0])   #Чтобы видить результат
#             print("Sugu on: ", sugu[ikood[0]])

#             aasta = sajand[ikood[0]] + str(ikood[1]) + str(ikood[2])
#             kuu = str(ikood[3]) + str(ikood[4])
#             paev = str(ikood[5]) + str(ikood[6])
#             sunni = f"{aasta}-{kuu}-{paev}"
#             print("Sünnipäev: ", sunni)

#             try:
#                 sunni_date = datetime.strptime(sunni, "%Y-%m-%d")
#                 print("Sünnipäev on korrektne: ", sunni_date.strftime("%d.%m.%Y"))
#             except:
#                 print("Sisestatud isikukoodis sünnipäев pole korrektne!")

#             ### Проверка исикукода (Взяла основу VBA, что делала дз Harjutus_4_Text_Date_Funk II)
#             s = [int(ikood[i]) for i in range(10)]
#             summ1 = sum(s[i] * (i + 1) for i in range(9)) + s[9] * 1 ##Цикл for i in range(9) необходим, чтобы, перебрать только первые 9 цифр списка s. Применить к каждой цифре её соответствующий множитель (1 для s[0], 2 для s[1], и так далее).
#             summ2 = sum(s[i] * arv[i] for i in range(10))  
#             jaak1 = summ1 % 11
#             jaak2 = summ2 % 11
#             if jaak1 != 10:   ###В случае, когда оба остатка jaak1 и jaak2 равны 10, это происходит из-за особенностей деления суммы на 11 и самого алгоритма проверки контрольного номера.
#                 kontrollnumber = jaak1
#             elif jaak2 != 10:   ### Пример: summ1 = 21, то 21 % 11 = 10 / summ2 = 32, то 32 % 11 = 10
#                 kontrollnumber = jaak2
#             else:
#                 kontrollnumber = 0    
            
#             if kontrollnumber == ikood[-1]:  ### используется индекс -1, чтобы обратиться к последнему элементу списка ikood / тобишь к ikood[10] тоже верно... Мы будем обращаться к последниму числу
#                 print(f"Kontrollnumber {kontrollnumber} õige!") 

#             ### Будем красиво высчитывать больницу
#             haigla = int(str(ikood[8]) + str(ikood[9]) + str(ikood[10])) ### т.к. потом мне нужен не тест а число, для диапазона чисел
#             print("Haiglatele määratud numbrid: ", haigla)
#             for vahemik, nimi in sunnitusmaja.items():    ###  Проверяем диапозоном есть ли такие числа в нашем списке
#                 if haigla in vahemik:
#                     haiglamaja = nimi
#                     print("Sünnimaja on: ", haiglamaja)
#         else:
#             print("Алustame uuesti")

#     else:
#         print("Isikukodus on 11 numbrit")
#         arvud.append(isik)
#         arvud.sort() 
#     print(f"Vimane isikukood oli: {isik},tema on {sugu[ikood[0]]}, tema sünnipäev on: {sunni_date.strftime("%d.%m.%Y")}, ta sündis: {haiglamaja}")
#     print("Praegu listis meil on:")
#     print("Isikukoodid: ", ikoodid)
#     print("Arvud: ", arvud)
