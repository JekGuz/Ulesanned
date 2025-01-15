import string
vokaalid = ["a","e","u","o","i","ü","ä","ö","õ"]
konsonanti = "qwrtypsdfghjklzxcvbnm"
markid = string.punctuation #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
v = k = m = t = 0
while True:
    tekst = input("Sisesta mingi tekst: ").lower()
    if tekst.isdigit():
        break
    else:
        tekst_list = list(tekst)
        print(tekst_list)
        for taht in tekst_list:
            if taht in vokaalid:
                v += 1
            elif taht in konsonanti:
                k += 1

