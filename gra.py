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

uzyte = []
def pytania():
    while True:
        losowe = random.randint(1,4)
        if losowe in uzyte:
            continue
        else:
            break
    
    uzyte.append(losowe)
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
        usun3 = usun2.replace(",", "")
        buton_a.set(usun3)
    kursor.execute(f"SELECT odp_b FROM pytania WHERE id = {losowe}")
    wynik_b = kursor.fetchall()
    for odp_bb in wynik_b:
        odp_bb = str(odp_bb)
        ah = odp_bb.replace("(", "")
        usun1 = ah.replace(")", "")
        usun2 = usun1.replace("'", "")
        usun3 = usun2.replace(",", "")
        buton_b.set(usun3)
    kursor.execute(f"SELECT odp_c FROM pytania WHERE id = {losowe}")
    wynik_c = kursor.fetchall()
    for odp_cc in wynik_c:
        odp_cc = str(odp_cc)
        ah = odp_cc.replace("(", "")
        usun1 = ah.replace(")", "")
        usun2 = usun1.replace("'", "")
        usun3 = usun2.replace(",", "")
        buton_c.set(usun3)
    kursor.execute(f"SELECT odp_d FROM pytania WHERE id = {losowe}")
    wynik_d = kursor.fetchall()
    for odp_dd in wynik_d:
        odp_dd = str(odp_dd)
        ah = odp_dd.replace("(", "")
        usun1 = ah.replace(")", "")
        usun2 = usun1.replace("'", "")
        usun3 = usun2.replace(",", "")
        buton_d.set(usun3)

pytania()


tekst_pytanie = tk.Label(root, textvariable=pytanie_tekst).pack()
button_a = tk.Button(root, textvariable=buton_a, command=lambda:pytania()).pack()
button_b = tk.Button(root, textvariable=buton_b, command=lambda:pytania()).pack()
button_c = tk.Button(root, textvariable=buton_c, command=lambda:pytania()).pack()
button_d = tk.Button(root, textvariable=buton_d, command=lambda:pytania()).pack()

root.mainloop()
connection.close()