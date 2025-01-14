# # Ülesanne 1 (Koos vidoe)
# spisok = [] # пустой список
# numbers = [1, 2, 3, 4, 5]
# abc = ["Abc", "B", "C"]
# slovo = "Programmeerimine"
# slovo_list = list(slovo)
# print(slovo)
# print(slovo_list)
# while True:
#     print("1 - добавить букву в список")
#     print("2 - склеить/соединить список\n3 - добавить букву на i - позицию")
#     print("4 - удалить элемент")
#     valik = int(input()) 
#     if valik == 1:
#         a = input("Введите букву: ")
#         slovo_list.append(a)
#         print(f"Добавили {a} новый список", slovo_list)
#     elif valik == 2:
#         slovo_list.extend(abc)
#         print(slovo_list)
#     elif valik == 3:
#         a = input("Введите букву, которую хочешь добавить: ")
#         i = int(input("ВВедите позицию, куда хочешь добавить букву: "))
#         slovo_list.insert(i-1,a)
#         print(slovo_list)
#     elif valik == 4:
#         a = input("Введите букву, которую хочешь удалить: ")
#         n = slovo_list.count(a)
#         print("Количесво букв, которые содержать введеную букву ", n)
#         if n > 0:
#             for i in range(n):
#                 slovo_list.remove(a)
#         else: 
#             print("Искомой буквы нет")
#         print(slovo_list)



# # Ülesanne oma varian kuidas kasutada Listis
# print("Alustame listi teha:")
# s6na_list = []
# try:
#     N = int(input("Kui palju sõnad kirjutame? "))
# except:
#     print("Midagi läks valesti")
# for i in range(N+1):
#     s6na = input("Sõna: ")  # запрашиваем слово
#     s6na_list.append(s6na)  # добавляем слово
#     print(f"Listis on nüüd: {s6na_list}") 
# print(f"Lõplik list: {s6na_list}")

# Ülesanne i
veel_list = ["Arvuti", "Hiir", "Klaaviatur", "Monitor"]
s6na_list = ["Leib", "Saike", "Kass", "Koer"]
while True:
    print("Meil on selline nimekiri: ", s6na_list)
    print("1 - lisage loendisse sõna\n2 - liimige/ühendage loend\n3 - lisage sõna i - positsioonile")
    print("4 - eemaldab elemendi\n5 - Laiendab loendit\n6 - sõnade arv loendis\n7 - lõpeta")
    try:
        valik = int(input()) 
        if valik == 1:
            a = str(input("Sisestage sõna: "))
            s6na_list.append(a.title())
            print(f"Lisatud {a.title()} uus nimikiri", s6na_list)
        elif valik == 2:
            s6na_list.extend(veel_list)
            print(s6na_list)
        elif valik == 3:
            a = str(input("Sisestage sõna, mida soovite lisada: "))
            i = int(input("Juhtige positsioon, kuhu soovite sõna lisada: "))
            s6na_list.insert(i-1,a.title())
            print(s6na_list)
        elif valik == 4:
            a = str(input("Sisestage sõna, mida soovite kustutada: ")).title()
            n = s6na_list.count(a)
            print("Selliste sõnade arv", n)
            if n > 0:
                for i in range(n):
                    s6na_list.remove(a)
            else: 
                print("Sõna, mida otsite, pole loendis")
            print(s6na_list)
        elif valik == 5:
            s6na_list.reverse()
            print(s6na_list)
        elif valik == 6:        
            print("Sõnade arv loendis", len(s6na_list))
        elif valik == 7:
            break
    except:
        print("Midagi läks valvasti")