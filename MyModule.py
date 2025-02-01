
#Ver 0
loginid = []
paroolid = []
while True:
    print("Kas te olite registrerituud? (Y/N)")
    vasta1 = str(input(": "))
    if vasta1.upper() == "Y":
        login = input("Sisesta oma login: ")
        #kontroll listis
        pasw = input("Siseta oma parool: ")
        #kontroll listis
        if login in loginid:
            print("Õige te olite sisestatu")
        else:
            print("Proovi uuesti")

    elif vasta1.upper() == "N":
        print("Soovite registreriida? (Y/N)")
        vasta2 = str(input(": "))

        if vasta2.upper() == "Y":
            login = input("Sisesta oma login: ")
            loginid.append(login)
            pasw = input("Siseta oma parool: ")
            paroolid.append(pasw)
            print("Nüüd te olite registreritud!")
        else:
            print("Nagemiseni!")
            break


