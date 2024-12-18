#3. Pärast treeningutega alustamist jooksis sportlane esimesel 
#päeval 10 km. Iga päev suurendas ta oma päevanormi 10% 
#võrra eelmise päeva normist. Kui palju on kogu distants, 
#mille sportlane 7 päeva jooksul läbib?

# km = 10
# S = 0
# print("Treenigute sportlane")
# for i in range(1,8,1):
#     km = (km * 0.1) + km
#     S = S + km
#     print(f"{i} - {round(S, 2)}")


i = 1
km = 10
S = 0
while i < 8:
    km = (km * 0.1) + km
    S = S + km
    print(f"{i} - {round(S, 2)}")
    i += 1
