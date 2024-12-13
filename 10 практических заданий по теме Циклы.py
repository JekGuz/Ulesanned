
# #Ülesanne 1
# try:
#     for i in range(1, 16):
#         n = float(input(f"{i}. samm sisesta arv: "))
#         if n.is_integer():
#             print(f"Täisarv {round(n)}")
#         else:
#             print(f"Murdarv {n}")
# except:
#     print("Sisesta arv")

#Ülesanne 2
# while True:
#     try:
#         A = int(input("Sisesta A: "))
#         break # Прирывания цикла!

#     except:
#         print("On vaja nuturaalne arv!")
# summa = 0
# if A > 0:
#     for i in range(1, A + 1, 1):
#         summa += i # сумма равна сумма + и (сумма равна и)
#         print(f"{i}. samm summa = {summa}")
#     print(f"Vastus {summa}")

# #Ülesanne 3
# p = 1
# for j in range(1,9,1): # можно написать range(8)
#     while True:
#         try:
#             arv = float(input("Sisesta arv: "))
#             break # Прирывания цикла!
#         except:
#             print("On vaja nuturaalne arv!")
#     if arv > 0: 
#         p*=arv
#     else:
#         print("Korrutame arvud rohkem kui 0")
#     print(f"{j}. samm korrutis = {p}")
# print(f"Lõpptulemus on {p}")

# #Ülesanne 3
# try:
#     for i in range(1, 9):
#         n = float(input(f"{i}. samm sisesta arv: "))
#         if n > 0:
#             n1 = n + n
#             print(f"Vastus: {round(n1)}")
# except:
#     print("Sisesta arv")

# #Ülesanne 4
# for i in range(10,21,1): 
#     print(i**2, end = ", ")
# print()

# #Ülesanne 5
# N = int(input("Sisestage, mitu korda küsime numbreid: "))
# for i in range(1,N+1,1):
#     try:
#         a = float(input(f"{i}.Sisesta negatiivne arv: "))
#         if a < 0:
#             n = a + a
#             print(f"{i}. summa: {round(n, 2)}")
#         else:
#             print(f"{i}.Arvutame ainult negatiivseid numbreid")
#     except:
#         print("Viga")

# #Ülesanne 6
# N = int(input("Sisestage, mitu korda küsime numbreid: "))
# for i in range(1,N+1,1):
#     try:
#        a = float(input(f"{i}.Sisesta arv: "))
#        if a < 0:
#            print(f"{i}.See on negatiivne arv: {a}")
#        elif a > 0:
#            print(f"{i}.See on positiivne arv: {a}")
#        else:
#             print(f"{i}.See on {a}")
#     except:
#         print("Midagi läks viga!")

# #Ülesanne 7
# try:
#     A = int(input("Sisestage vahemiku algus (A): "))
#     B = int(input("Sisestage vahemiku algus (B): "))
#     K = int(input("Sisesta arv K: "))
#     if K == 0:
#         print("Te ei saa 0-ga jagada")
#     elif A == B:
#         print(f"Vahemik ei saa olla võrdne {A} - {B}")
#     else:
#         print(f"Numbrid vahemikust {A} - {B}, arvu {K} kordsed")
#         for i in range(A+1,B+1,1):
#             if i % K == 0:  # Проверяем кратность
#                 print(i, end = " ")
#         print()    # пропробовала print() сначала под print(i, end = " ") не понравилось, потом под if стало хуже, решила под for
# except:
#     print("Midagi läks viga!")

# # #Ülesanne 8
# for i in range(1,21,1):
#     sm = i * 2.5   #дюйм 2.54
#     print(f"{i} - {round(sm, 2)}")

# #Ülesanne 9
# try:
#     N = int(input("Mitmeks aastaks me summa paneme?: "))
#     S = float(input("Misugune summa: "))
#     for i in range(1,21,1):
#         sm = i * 0.3
#         print(f"{i} - {round(sm, 2)}")
# except:
#     print("Midagi läks vale.")

# #Ülesanne 16
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i == j:
#             print(j, end = " ")
#         else:
#             print(0, end = " ")
#     print()  # enter
# print()

# #Ülesanne 15
# for i in range(0, 10):
#     for j in range(0, 10):
#         print(j, end = " ")
#     print()
# print()

