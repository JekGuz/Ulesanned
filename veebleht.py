from tkinter import *
from gtts import *
import smtplib, ssl
from email.message import EmailMessage
from tkinter import filedialog
import imghdr
from tkinter import messagebox
from PIL import Image, ImageTk


file = None  # Глобальная переменная для хранения

def vali_pilt():
    """
    Valime pilt
    """
    global file
    file = filedialog.askopenfilename()
    if file:
        lisa_text.configure(text=file)  # меняем текст lisa_text
    return file

def saada_kiri():
    """
    Saadame kiri
    """
    global file
    kellele = email_text.get().strip().split(",")    # добавить несколько пользователей
    kiri = kiri_text.get("1.0", END).strip()
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "kotikj89@gmail.com"
    password = "xtjr iomj prvr orzr"  
    
    # Проверки перед отправкой
    if not kellele:
        messagebox.showerror("Tekkis viga!", "Palun sisesta e-posti aadress!")
        return
    
    if not file:
        messagebox.showerror("Tekkis viga!", "Palun vali pilt enne kirja saatmist!")
        return
    
    context = ssl.create_default_context()
    
    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = "E-kiri saatmine"
    msg['From'] = "Jekaterina Guzek"
    msg['To'] = kellele
    
    try:
        with open(file, 'rb') as fpilt:
            pilt = fpilt.read()
        msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))
    except Exception as e:
        messagebox.showerror("Tekkis viga!", f"Pildi lisamine ebaõnnestus: {e}")
        return
    
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("Informatsioon", "Kiri oli saadetud")
    except Exception as e:
        messagebox.showerror("Tekkis viga!", f"Kirja saatmine ebaõnnestus: {e}")
    finally:
        server.quit()

def puhastamine():
    """
    Puhastame kõik väljad
    """
    global file 
    email_text.delete(0, END)  # удаляем значение в поле email_text  0 - начальная позиция
    teema_text.delete(0, END)  # END – конечная позиция (весь текст будет удалён)
    kiri_text.delete("1.0", END) # 1.0 - первая строка нулевой симфол END все удаляем
    file = None
    lisa_text.configure(text="...") # меняем в поле lisa_text - на ...

def lisa_allkiri():
    """
    Lisab allkirja kirja lõppu
    """
    kiri_text.insert(END, "\n\n" + "Parimate soovidega,\nJekaterina Guzek")   # END -  добавляем подпись в конец с 

aken = Tk()
aken.geometry("600x600")
aken.resizable(False, False)
aken.title("Veeb")

# Добавляем картинку (фон)
original_pilt = Image.open(r"C:\Users\kotik\source\repos\Ulesanned\leht.jpg")
resize_pilt = original_pilt.resize((600, 600))
bgpilt = ImageTk.PhotoImage(resize_pilt)

# Устанавливаем фон
labelBg = Label(aken, image=bgpilt)
labelBg.place(x=0, y=0, relwidth=1, relheight=1) 


# Окна добаляем
Label(aken, text="Email:", font=("Times New Roman", 18), fg="white",bg="green", padx=30).grid(row=0, column=0)

email_text = Entry(aken, font=("Times New Roman", 18), fg="black", bg="#95da96", width=27)
email_text.grid(row=0, column=1, padx=40)

Label(aken, text="Teema:", font=("Times New Roman", 18), fg="white",bg="green", padx=26).grid(row=1, column=0)

teema_text = Entry(aken, font=("Times New Roman", 18), fg="black", bg="#95da96", width=27)
teema_text.grid(row=1, column=1, padx=40)

Label(aken, text="Lisa:", font=("Times New Roman", 18), fg="white",bg="green", padx=38).grid(row=2, column=0)

lisa_text = Label(aken, text="...", font=("Times New Roman", 7), padx=38)
lisa_text.grid(row=2, column=1, padx=40)

Label(aken, text="Kiri:", font=("Times New Roman", 18), fg="white",bg="green", padx=38).grid(row=3, column=0)

kiri_text = Text(aken, font=("Times New Roman", 18), fg="black", bg="#95da96", width=27, height=6)
kiri_text.grid(row=3, column=1)

# Кнопки добавляем
Button(text="LISA PILT", font=("Times New Roman", 18), fg="white",bg="green", command=vali_pilt).place(x=20, y=290)    #.grid(row=5, column=0)
Button(text="SAADA", font=("Times New Roman", 18), fg="white",bg="green", command=saada_kiri).place(x=160, y=290)        #.grid(row=5, column=1)
Button(text="PUHASTA", font=("Times New Roman", 18), fg="white",bg="red", command=puhastamine).place(x=270, y=290)       #.grid(row=5, column=2)
Button(text="ALLKIRI", font=("Times New Roman", 18), fg="white",bg="blue", command=lisa_allkiri).place(x=410, y=290)



aken.mainloop()
