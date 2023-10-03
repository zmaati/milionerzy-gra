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

    for a in wynik:
        print(a)

pytania()


tekst_pytanie = tk.Label(root, text=pytanie_tekst).pack()
button_a = tk.Button(root, textvariable=buton_a).pack()
button_b = tk.Button(root, textvariable=buton_b).pack()
button_c = tk.Button(root, textvariable=buton_c).pack()
button_d = tk.Button(root, textvariable=buton_d).pack()

root.mainloop()
connection.close()