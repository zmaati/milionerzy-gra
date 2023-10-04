import tkinter as tk # grafika
import mysql.connector as baza # baza danych
import random # losowanie pytań
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
root = tk.Tk()
root.title("Milionerzy")
root.geometry("800x600")
# Zmienne do labeli oraz przycisków
pytanie_tekst = tk.StringVar()
PrzyciskOdp_A = tk.StringVar()
PrzyciskOdp_B = tk.StringVar()
PrzyciskOdp_C = tk.StringVar()
PrzyciskOdp_D = tk.StringVar()
pieniadze_var = tk.IntVar()
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
        usun_nawias_o = tresc_pytania.replace("(", "")
        usun_nawias_z = usun_nawias_o.replace(")", "")
        usun_apostrof = usun_nawias_z.replace("'", "")
        koncowy_tekst_pytanie_1 = usun_apostrof.replace(",", "")
        pytanie_tekst.set(koncowy_tekst_pytanie_1)
    
    # Wykonanie komendy SELECT po odpowiedź A
    zapytanie.execute(f"SELECT odp_a FROM pytania WHERE id = {losowe}")
    wynik_a = zapytanie.fetchall()
    for tresc_odpowiedzi_a in wynik_a:
        tresc_odpowiedzi_a = str(tresc_odpowiedzi_a)
        usun_nawias_o_2 = tresc_odpowiedzi_a.replace("(", "")
        usun_nawias_z_2 = usun_nawias_o_2.replace(")", "")
        usun_apostrof_2 = usun_nawias_z_2.replace("'", "")
        global odpowiedz_A
        odpowiedz_A = usun_apostrof_2.replace(",", "")
        PrzyciskOdp_A.set(odpowiedz_A)
    
    # Wykonanie komendy SELECT po odpowiedź B
    zapytanie.execute(f"SELECT odp_b FROM pytania WHERE id = {losowe}")
    wynik_b = zapytanie.fetchall()
    for tresc_odpowiedzi_b in wynik_b:
        tresc_odpowiedzi_b = str(tresc_odpowiedzi_b)
        usun_nawias_o_3 = tresc_odpowiedzi_b.replace("(", "")
        usun_nawias_z_3 = usun_nawias_o_3.replace(")", "")
        usun_apostrof_3 = usun_nawias_z_3.replace("'", "")
        global odpowiedz_B
        odpowiedz_B = usun_apostrof_3.replace(",", "")
        PrzyciskOdp_B.set(odpowiedz_B)
    
    # Wykonanie komendy SELECT po odpowiedź C
    zapytanie.execute(f"SELECT odp_c FROM pytania WHERE id = {losowe}")
    wynik_c = zapytanie.fetchall()
    for tresc_odpowiedzi_c in wynik_c:
        tresc_odpowiedzi_c = str(tresc_odpowiedzi_c)
        usun_nawias_o_4 = tresc_odpowiedzi_c.replace("(", "")
        usun_nawias_z_4 = usun_nawias_o_4.replace(")", "")
        usun_apostrof_4 = usun_nawias_z_4.replace("'", "")
        global odpowiedz_C
        odpowiedz_C = usun_apostrof_4.replace(",", "")
        PrzyciskOdp_C.set(odpowiedz_C)
    
    # Wykonanie komendy SELECT po odpowiedź D
    zapytanie.execute(f"SELECT odp_d FROM pytania WHERE id = {losowe}")
    wynik_d = zapytanie.fetchall()
    for tresc_odpowiedzi_d in wynik_d:
        tresc_odpowiedzi_d = str(tresc_odpowiedzi_d)
        usun_nawias_o_5 = tresc_odpowiedzi_d.replace("(", "")
        usun_nawias_z_5 = usun_nawias_o_5.replace(")", "")
        usun_apostrof_5 = usun_nawias_z_5.replace("'", "")
        global odpowiedz_D
        odpowiedz_D = usun_apostrof_5.replace(",", "")
        PrzyciskOdp_D.set(odpowiedz_D)
        
    
    
    # Wykonanie komendy SELECT po poprawną odpowiedź
    zapytanie.execute(f"SELECT pop_odp FROM pytania WHERE id = {losowe}")
    wynik_poprawna_odpowiedz = zapytanie.fetchall()
    for tresc_poprawnej_odpowiedzi in wynik_poprawna_odpowiedz:
        tresc_poprawnej_odpowiedzi = str(tresc_poprawnej_odpowiedzi)
        usun_nawias_o_6 = tresc_poprawnej_odpowiedzi.replace("(", "")
        usun_nawias_z_6 = usun_nawias_o_6.replace(")", "")
        usun_apostrof_6 = usun_nawias_z_6.replace("'", "")
        global koncowy_tekst_poprawnej_odpowiedzi
        koncowy_tekst_poprawnej_odpowiedzi = usun_apostrof_6.replace(",", "")
        print(koncowy_tekst_poprawnej_odpowiedzi)
# OD TAD TRZEBA DOKONCZYC OK OK OK OK
# TRZEBA TYLKO ZROBIC TEN SYSTEM PIENIEDZY I GIT
# JUZ DZIALAJA DOBRE I ZLE ODPOWIEDZI
    global pieniadze
    global liczba
    pieniadze = [0,500,1000,2000,5000,10000,20000,40000,75000,125000,250000,500000,1000000]
    liczba = 0
    
def sprawdz_przycisk_a():
    if (koncowy_tekst_poprawnej_odpowiedzi == odpowiedz_A):
        print("Przycisk A Działa")
        pytania()
    else:
        root.destroy()
def sprawdz_przycisk_b():
    if (koncowy_tekst_poprawnej_odpowiedzi == odpowiedz_B):
        print("Przycisk B Działa")
        pytania()
    else:
        root.destroy()
def sprawdz_przycisk_c():
    if (koncowy_tekst_poprawnej_odpowiedzi == odpowiedz_C):
        print("Przycisk C Działa")
        pytania()
    else:
        root.destroy()
def sprawdz_przycisk_d():
    if (koncowy_tekst_poprawnej_odpowiedzi == odpowiedz_D):
        print("Przycisk D Działa")
        pytania()
    else:
        root.destroy()
pytania()

pieniadze = tk.Label(root, textvariable=pieniadze_var).pack()
tekst_pytanie = tk.Label(root, textvariable=pytanie_tekst).pack()
buton_1 = tk.Button(root, textvariable=PrzyciskOdp_A, command=lambda:sprawdz_przycisk_a()).pack()
buton_2 = tk.Button(root, textvariable=PrzyciskOdp_B, command=lambda:sprawdz_przycisk_b()).pack()
buton_3 = tk.Button(root, textvariable=PrzyciskOdp_C, command=lambda:sprawdz_przycisk_c()).pack()
buton_4 = tk.Button(root, textvariable=PrzyciskOdp_D, command=lambda:sprawdz_przycisk_d()).pack()

root.mainloop()
connection.close()