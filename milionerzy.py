import tkinter as tk # grafika
from tkinter import messagebox as msg
from tkinter import font as tkFont
import mysql.connector as baza # baza danych
import random # losowanie pytań
import matplotlib.pyplot as plt # matplotlib
import numpy as np
from PIL import Image, ImageTk
# Zmienne, które się podaje podczas łączenia
host = "localhost"
user = "root"
password = ""
baza_danych = "milionerzy"
# Łączenie z bazą danych
connection = baza.connect(
    host=host,
    user=user,
    password=password,
    database = baza_danych
)
# Ustawienie okna tkinter

okno = msg.askquestion("Milionerzy", "Czy chcesz zacząć grę w milionerów?")
root = tk.Tk()
root.title("Milionerzy")
root.geometry("900x600")
root.resizable(False, False)

if okno == 'no':
    root.destroy()

root.after(1, root.focus_force)

# Zmienne do labeli oraz przycisków
pytanie_tekst = tk.StringVar()
PrzyciskOdp_A = tk.StringVar()
PrzyciskOdp_B = tk.StringVar()
PrzyciskOdp_C = tk.StringVar()
PrzyciskOdp_D = tk.StringVar()
pieniadze_var = tk.IntVar()
telefon_var = tk.StringVar()
pieniadze_var.set(0)
# Pusta lista do użytych juz pytań (resetuje sie po ponownym wystartowaniu gry)
uzyte = []

def pytania():
    # losowanie pytań
    # (Losowanie id pytania)
    while True:
        global losowe
        losowe = random.randint(1,25)
        if losowe in uzyte: # Jeżeli pytanie zostało już uzyte niech dalej losuje
            continue
        else: # Jeżeli nie to koniec losowania
            break

    # Dodawanie użytych pytan do listy uzyte (28 linia)
    uzyte.append(losowe)

    # Umożliwia korzystanie z komend SQL
    global zapytanie
    zapytanie = connection.cursor()

    # Wykonanie komendy SELECT za pomocą cursor()
    zapytanie.execute(f"SELECT tresc FROM pytania WHERE id = {losowe}")

    # Wybieranie wyników z SELECT
    wynik = zapytanie.fetchall()
    for tresc_pytania in wynik:
        tresc_pytania = str(tresc_pytania)
        koncowy_tekst_pytanie_1 = tresc_pytania.strip('(),\'')
        pytanie_tekst.set(koncowy_tekst_pytanie_1)
    # Wykonanie komendy SELECT po odpowiedź A
    zapytanie.execute(f"SELECT odp_a FROM pytania WHERE id = {losowe}")
    wynik_a = zapytanie.fetchall()
    for tresc_odpowiedzi_a in wynik_a:
        tresc_odpowiedzi_a = str(tresc_odpowiedzi_a)
        global odpowiedz_A
        odpowiedz_A = tresc_odpowiedzi_a.strip('(),\'')
        PrzyciskOdp_A.set("A. " + odpowiedz_A)
    # Wykonanie komendy SELECT po odpowiedź B
    zapytanie.execute(f"SELECT odp_b FROM pytania WHERE id = {losowe}")
    wynik_b = zapytanie.fetchall()
    for tresc_odpowiedzi_b in wynik_b:
        tresc_odpowiedzi_b = str(tresc_odpowiedzi_b)
        global odpowiedz_B
        odpowiedz_B = tresc_odpowiedzi_b.strip('(),\'')
        PrzyciskOdp_B.set("B. " + odpowiedz_B)
    # Wykonanie komendy SELECT po odpowiedź C
    zapytanie.execute(f"SELECT odp_c FROM pytania WHERE id = {losowe}")
    wynik_c = zapytanie.fetchall()
    for tresc_odpowiedzi_c in wynik_c:
        tresc_odpowiedzi_c = str(tresc_odpowiedzi_c)
        global odpowiedz_C
        odpowiedz_C = tresc_odpowiedzi_c.strip('(),\'')
        PrzyciskOdp_C.set("C. "+ odpowiedz_C)
    # Wykonanie komendy SELECT po odpowiedź D
    zapytanie.execute(f"SELECT odp_d FROM pytania WHERE id = {losowe}")
    wynik_d = zapytanie.fetchall()
    for tresc_odpowiedzi_d in wynik_d:
        tresc_odpowiedzi_d = str(tresc_odpowiedzi_d)
        global odpowiedz_D
        odpowiedz_D = tresc_odpowiedzi_d.strip('(),\'')
        PrzyciskOdp_D.set("D. " + odpowiedz_D)
    # Wykonanie komendy SELECT po poprawną odpowiedź
    zapytanie.execute(f"SELECT pop_odp FROM pytania WHERE id = {losowe}")
    wynik_poprawna_odpowiedz = zapytanie.fetchall()
    for tresc_poprawnej_odpowiedzi in wynik_poprawna_odpowiedz:
        tresc_poprawnej_odpowiedzi = str(tresc_poprawnej_odpowiedzi)
        global koncowy_tekst_poprawnej_odpowiedzi
        koncowy_tekst_poprawnej_odpowiedzi = tresc_poprawnej_odpowiedzi.strip('(),\'')
        # print(koncowy_tekst_poprawnej_odpowiedzi)
        # Sprawdzanie odpowiedzi ^

nrIndeks = 0
def pieniadze_function():
    global nrIndeks
    global pieniadze_var1
    pieniadze = [0,500,1000,2000,5000,10000,20000,40000,75000,125000,250000,500000,1000000]
    nrIndeks += 1
    pieniadze_var.set(str(pieniadze[nrIndeks]))
    if nrIndeks >= 12:
        wygrana = msg.showinfo("Gratulacje!", "Gratulacje użytkowniku wygrałeś milion złoty!")
        if wygrana == 'ok':
            root.destroy()
def AktywujPrzyciski():
    odp_a.config(state="active")
    odp_b.config(state="active")
    odp_c.config(state="active")
    odp_d.config(state="active")

def sprawdz_odpowiedz(odpowiedz):
    if koncowy_tekst_poprawnej_odpowiedzi == odpowiedz:
        pieniadze_function()
        pytania()
        AktywujPrzyciski()
    else:
        if str(pieniadze_var.get()) != "0":
            zla_odpowiedz_message = f"Wybrałeś/aś złą odpowiedź.\nUdało ci się wygrać {pieniadze_var.get()} PLN"
            zla_odpowiedz = msg.showwarning("Koniec gry", zla_odpowiedz_message)
            if zla_odpowiedz == 'ok':
                root.destroy()
        else:
            za_zero = msg.showwarning("Koniec gry", "Wybrałeś/aś złą odpowiedź.\nNiestety wychodzisz dzisiaj z niczym")
            if za_zero == 'ok':
                root.destroy()

# Now use the single function for all the buttons
def sprawdz_przycisk_a():
    sprawdz_odpowiedz(odpowiedz_A)

def sprawdz_przycisk_b():
    sprawdz_odpowiedz(odpowiedz_B)

def sprawdz_przycisk_c():
    sprawdz_odpowiedz(odpowiedz_C)

def sprawdz_przycisk_d():
    sprawdz_odpowiedz(odpowiedz_D)


pytania()

def TelefonDoPrzyjaciela():
    msg.showinfo("Przyjaciel",f"Przyjaciel podpowiada, że {koncowy_tekst_poprawnej_odpowiedzi} to poprawna odpowiedź.")
    Telefon.config(state="disabled")

def PolNaPol_Funkcja():
    niepoprawne = [odpowiedz_A, odpowiedz_B, odpowiedz_C, odpowiedz_D]
    niepoprawne.remove(koncowy_tekst_poprawnej_odpowiedzi)
    wybrane = random.sample(niepoprawne, 2)

    if odpowiedz_A in wybrane:
        odp_a.config(state="disabled")
    if odpowiedz_B in wybrane:
        odp_b.config(state="disabled")
    if odpowiedz_C in wybrane:
        odp_c.config(state="disabled")
    if odpowiedz_D in wybrane:
        odp_d.config(state="disabled")

    PolNaPol.config(state="disabled")

def Publicznosc_Funkcja():
    if odpowiedz_A == koncowy_tekst_poprawnej_odpowiedzi:
        wykres("A")
    if odpowiedz_B == koncowy_tekst_poprawnej_odpowiedzi:
        wykres("B")
    if odpowiedz_C == koncowy_tekst_poprawnej_odpowiedzi:
        wykres("C")
    if odpowiedz_D == koncowy_tekst_poprawnej_odpowiedzi:
        wykres("D")

# Funkcja tworząca wykres "Wynik publiczności"
def wykres(odp):
    mylabels = ["A", "B", "C", "D"] # Nazwy, które pojawią się przy wykresie
    if odp == "A":
        y = np.array([39, 11, 25, 15]) 
        myexplode = [0.2, 0, 0, 0]
    elif odp == "B":
        y = np.array([15, 45, 25, 15])
        myexplode = [0, 0.2, 0, 0]
    elif odp == "C":
        y = np.array([10, 10, 60, 20])
        myexplode = [0, 0, 0.2, 0]
    else:
        y = np.array([10, 20, 20, 50])
        myexplode = [0, 0, 0, 0.2]

    plt.title("Wyniki publiczności")
    plt.pie(y, labels = mylabels, explode = myexplode)
    plt.show() 
    Publicznosc.config(state="disabled")

#graficzka


obraz = Image.open("do graficzki.gif")
tlo_obraz = ImageTk.PhotoImage(obraz)
czcionka = tkFont.Font(family='Impact', size=20, weight='bold')

# Widgety
image = Image.open("do graficzki.gif")  # Zmień na odpowiednią ścieżkę do swojego obrazu

# Konwertuj obraz PIL na obiekt PhotoImage
photo = ImageTk.PhotoImage(image)

# Ustaw tło canvasa na obraz PhotoImage
canvas = tk.Canvas(root, width=900, height=600)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

tlo_label = tk.Label(root, image=tlo_obraz)
tlo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Wypełnij całe okno

ramka_lewa = tk.Frame(tlo_label)
ramka_prawa = tk.Frame(tlo_label)
ramka_lewa.pack(side="left", padx=20)
ramka_prawa.pack(side="right", padx=20)

ramkanic = tk.Frame(tlo_label)
ramkanic.pack(side="top",padx=20)

ramka_srodek = tk.Frame(tlo_label)
ramka_srodek.pack(side="bottom", padx=20)

pieniadze = tk.Label(root, textvariable=pieniadze_var,font=czcionka,bg="dark blue",fg="#F8C653")
tekst_pytanie = tk.Label(root, textvariable=pytanie_tekst,font=czcionka,bg="Dark Blue",fg="#F8C653")
czcionka = tkFont.Font(family='Impact', size=20, weight='bold')

odp_a = tk.Button(root, textvariable=PrzyciskOdp_A, command=lambda:sprawdz_przycisk_a(),bg="dark blue",font=czcionka,fg="yellow", width=20)
odp_b = tk.Button(root, textvariable=PrzyciskOdp_B, command=lambda:sprawdz_przycisk_b(),bg="dark blue",font=czcionka,fg="yellow", width=20)
odp_c = tk.Button(root, textvariable=PrzyciskOdp_C, command=lambda:sprawdz_przycisk_c(),bg="dark blue",font=czcionka,fg="yellow", width=20)
odp_d = tk.Button(root, textvariable=PrzyciskOdp_D, command=lambda:sprawdz_przycisk_d(),bg="dark blue",font=czcionka,fg="yellow", width=20)
Telefon = tk.Button(root, text="Telefon do przyjaciela", command=lambda:TelefonDoPrzyjaciela(),bg="dark blue",font=czcionka, width=20,fg="#F8C653")
PolNaPol = tk.Button(root, text="50/50", command=lambda:PolNaPol_Funkcja(),bg="dark blue",font=czcionka, width=15,fg="#F8C653")
Publicznosc = tk.Button(root, text="Publiczność",command=lambda:Publicznosc_Funkcja(),bg="dark blue",font=czcionka, width=15,fg="#F8C653")

# Wyświetlanie widgetów
odpa_wyswietl = canvas.create_window(146, 250, window=odp_a)
odpb_wyswietl = canvas.create_window(756,250, window=odp_b)
odpc_wyswietl = canvas.create_window(146,310, window=odp_c)
odpd_wyswietl = canvas.create_window(756,310, window=odp_d)
PolNaPol_wyswietl = canvas.create_window(110,500, window=PolNaPol)
Telefon_wyswietl = canvas.create_window(470,500, window=Telefon)
Publicznosc_wyswietl = canvas.create_window(792,500, window=Publicznosc)
pytanie_wyswietl = canvas.create_window(470,50, window=tekst_pytanie)
Spacja = tk.Label(root, text="").pack()
pieniadze_wyswietl = canvas.create_window(470,80, window=pieniadze)
# Ustalenie, żeby przyciski nie traciły koloru po wciśnięciu
odp_a['activebackground'] = "dark blue"
odp_b['activebackground'] = "dark blue"
odp_c['activebackground'] = "dark blue"
odp_d['activebackground'] = "dark blue"
odp_a['activeforeground'] = "yellow"
odp_b['activeforeground'] = "yellow"
odp_c['activeforeground'] = "yellow"
odp_d['activeforeground'] = "yellow"
root.mainloop()
connection.close()