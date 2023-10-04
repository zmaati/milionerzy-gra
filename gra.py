import tkinter as tk
import mysql.connector as baza
import random

host = "localhost"
user = "root"
password = ""
baza_danych = "milionerzy2dt"

connection = baza.connect(
    host=host,
    user=user,
    password=password,
    database = baza_danych
)
root = tk.Tk()
root.title("Milionerzy")
root.geometry("400x400")

pytanie_tekst = tk.StringVar()
buton_a = tk.StringVar()
buton_b = tk.StringVar()
buton_c = tk.StringVar()
buton_d = tk.StringVar()
pieniadze_var = tk.IntVar()
CheckButton1_var = tk.IntVar()
CheckButton2_var = tk.IntVar()
CheckButton3_var = tk.IntVar()
CheckButton4_var = tk.IntVar()

uzyte = []
def pytania():
    while True:
        global losowe
        losowe = random.randint(1,4)
        if losowe in uzyte:
            continue
        else:
            break
    
    uzyte.append(losowe)
    global kursor
    kursor = connection.cursor()
    kursor.execute(f"SELECT tresc FROM pytania WHERE id = {losowe}")
    wynik = kursor.fetchall()
    for x in wynik:
        x = str(x)
        a = x.replace("(", "")
        i = a.replace(")", "")
        k = i.replace("'", "")
        l = k.replace(",", "")
        pytanie_tekst.set(l)
    kursor.execute(f"SELECT odp_a FROM pytania WHERE id = {losowe}")
    wynik_a = kursor.fetchall()
    for odp_aa in wynik_a:
        odp_aa = str(odp_aa)
        ah = odp_aa.replace("(", "")
        usun1 = ah.replace(")", "")
        usun2 = usun1.replace("'", "")
        buton111 = usun2.replace(",", "")
        buton_a.set(buton111)
    global xd4
    xd4 = buton111
    kursor.execute(f"SELECT odp_b FROM pytania WHERE id = {losowe}")
    wynik_b = kursor.fetchall()
    for odp_bb in wynik_b:
        odp_bb = str(odp_bb)
        ah = odp_bb.replace("(", "")
        usun1 = ah.replace(")", "")
        usun2 = usun1.replace("'", "")
        buton333 = usun2.replace(",", "")
        buton_b.set(buton333)
    global xd3
    xd3 = buton333
    kursor.execute(f"SELECT odp_c FROM pytania WHERE id = {losowe}")
    wynik_c = kursor.fetchall()
    for odp_cc in wynik_c:
        odp_cc = str(odp_cc)
        ah = odp_cc.replace("(", "")
        usun1 = ah.replace(")", "")
        usun2 = usun1.replace("'", "")
        usun3 = usun2.replace(",", "")
        buton_c.set(usun3)
    global xd2
    xd2 = usun3
    kursor.execute(f"SELECT odp_d FROM pytania WHERE id = {losowe}")
    wynik_d = kursor.fetchall()
    for odp_dd in wynik_d:
        odp_dd = str(odp_dd)
        ah = odp_dd.replace("(", "")
        usun1 = ah.replace(")", "")
        usun2 = usun1.replace("'", "")
        buton444 = usun2.replace(",", "")
        buton_d.set(buton444)
    global xd
    xd = buton444
    kursor.execute(f"SELECT pop_odp FROM pytania WHERE id = {losowe}")
    poprawna_odp = kursor.fetchall()
    for pop_odp in poprawna_odp:
        pop_odp = str(pop_odp)

    pieniadze = [0,500,1000,2000,5000,10000,20000,40000,75000,125000,250000,500000,1000000]
    liczba = 0
    kursor.execute(f"SELECT pop_odp FROM pytania WHERE id = {losowe}")
    poprawna_odp = kursor.fetchall()
    for pop_odp in poprawna_odp:
        pop_odp = str(pop_odp)
        aha = odp_dd.replace("(", "")
        aha1 = aha.replace(")", "")
        aha2 = aha1.replace("'", "")
        aha3 = aha2.replace(",", "")
        global popr_odp
        popr_odp = aha3
        print(popr_odp)
    
def sprawdz_przycisk_a():
    if (popr_odp == xd4):
        print("xdd")
        pytania()
def sprawdz_przycisk_b():
    if (popr_odp == xd3):
        print("xdd222")
        pytania()
def sprawdz_przycisk_c():
    if (popr_odp == xd2):
        print("xdd333")
        pytania()
def sprawdz_przycisk_d():
    if (popr_odp == xd):
        print("xdd444")
        pytania()

pytania()
pieniadze = tk.Label(root, textvariable=pieniadze_var).pack()
tekst_pytanie = tk.Label(root, textvariable=pytanie_tekst).pack()
buton_1 = tk.Button(root, textvariable=buton_a, command=lambda:sprawdz_przycisk_a()).pack()
buton_2 = tk.Button(root, textvariable=buton_b, command=lambda:sprawdz_przycisk_b()).pack()
buton_3 = tk.Button(root, textvariable=buton_c, command=lambda:sprawdz_przycisk_c()).pack()
buton_4 = tk.Button(root, textvariable=buton_d, command=lambda:sprawdz_przycisk_d()).pack()

root.mainloop()
connection.close()