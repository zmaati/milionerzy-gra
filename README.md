# Dokumentacja gry “Milionerzy”

## 1. Wprowadzenie
Gra "Milionerzy" to projekt napisany w języku Python z wykorzystaniem biblioteki Tkinter do tworzenia interfejsu użytkownika oraz bazy danych MySQL do przechowywania pytań i odpowiedzi. Projekt umożliwia graczowi udział w wirtualnym teleturnieju "Milionerzy", w którym musi wybierać poprawne odpowiedzi na pytania i zdobywać nagrody pieniężne.

## 2. Instalacja
Aby uruchomić grę "Milionerzy", wykonaj następujące kroki:


Upewnij się, że masz zainstalowaną bibliotekę Tkinter, Python oraz serwer MySQL.

Skonfiguruj połączenie z bazą danych, dostosowując zmienne takie jak host, user, password, i baza_danych w kodzie.

Uruchom skrypt Pythona w swoim środowisku.

## 3. Uruchamianie

Po uruchomieniu gry, zostaniesz zapytany, czy chcesz zacząć grę w "Milionerów". Po potwierdzeniu, gra rozpocznie się, a Ty będziesz miał możliwość wyboru odpowiedzi na różne pytania. W grze dostępne są różne mechanizmy pomocy, takie jak "Telefon do przyjaciela", "50/50" i "Publiczność".


## 4. Opis Kodu
Kod gry "Milionerzy" składa się z różnych części. Oto krótki opis głównych elementów kodu:


### Importowanie modułów:
 W pierwszej części kodu importowane są niezbędne biblioteki, takie jak Tkinter, MySQL, NumPy itp.

### Łączenie z bazą danych:
 Następnie następuje połączenie z bazą danych MySQL.

### Ustawienie okna Tkinter:
 Okno Tkinter jest tworzone i przygotowywane dla użytkownika.

### Pytania:
 Funkcja pytania() losuje pytania z bazy danych i przygotowuje interfejs do wyświetlenia pytania oraz odpowiedzi.

### System pieniędzy:
 Gra obsługuje system pieniędzy, który jest zaktualizowany po poprawnej odpowiedzi.

### Funkcje do sprawdzania odpowiedzi:
 Każdy przycisk z odpowiedzią ma funkcję, która sprawdza, czy odpowiedź jest poprawna, aktualizuje pieniądze i przechodzi do kolejnego pytania.

### Mechanizmy pomocy:
 Gra obsługuje trzy mechanizmy pomocy: "Telefon do przyjaciela", "50/50" i "Publiczność". Odpowiednie funkcje są wywoływane po użyciu tych mechanizmów.

### Wykres "Wynik publiczności":
 Wykres ten jest tworzony przy użyciu biblioteki Matplotlib i wyświetla procentowy wynik publiczności dla odpowiedzi.


5. Zmienne
Oto lista wszystkich zmiennych używanych w kodzie gry "Milionerzy" wraz z krótkim opisem:


### host:
 Adres hosta serwera MySQL, do którego łączymy się.

### user:
 Nazwa użytkownika do logowania do serwera MySQL.

### password:
 Hasło użytkownika do logowania do serwera MySQL.

### baza_danych:
 Nazwa bazy danych, w której przechowujemy pytania.

### connection:
 Obiekt reprezentujący połączenie z bazą danych MySQL.

### okno:
 Okno dialogowe wykorzystywane do pytania o rozpoczęcie gry.

### pytanie_tekst:
 Zmienna przechowująca treść pytania.

### PrzyciskOdp_A, PrzyciskOdp_B, PrzyciskOdp_C, PrzyciskOdp_D:
 Zmienne przechowujące treść odpowiedzi A, B, C i D.

### pieniadze_var:
 Zmienna przechowująca informację o aktualnym stanie pieniędzy gracza.

### telefon_var:
 Zmienna przechowująca informację o wykorzystanym telefonie do przyjaciela.

### użyte:
 Lista przechowująca ID użytych już pytań (resetuje się po ponownym wystartowaniu gry).

### losowe:
 Zmienna przechowująca losowo wygenerowane ID pytania.

### zapytanie:
 Obiekt do komunikacji z bazą danych MySQL.

### wynik:
 Zmienna przechowująca wynik zapytania SQL dotyczącego treści pytania.

### tresc_pytania:
 Zmienna przechowująca treść pytania po pobraniu z bazy danych.

### odpowiedz_A, odpowiedz_B, odpowiedz_C, odpowiedz_D:
 Zmienne przechowujące treści odpowiedzi A, B, C i D.

### koncowy_tekst_poprawnej_odpowiedzi:
 Zmienna przechowująca treść poprawnej odpowiedzi na pytanie.

### liczba:
 Zmienna przechowująca liczbę, która zwiększa się po poprawnej odpowiedzi, służy do aktualizacji stanu pieniędzy.


6. Funkcje
### pytania():
Losuje pytania z bazy danych i przygotowuje interfejs.
przykład:

```
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
```


### pieniadze_function():
Aktualizuje stan pieniędzy.
przykład:

```
def pieniadze_function():
        pieniadze = [0,500,1000,2000,5000,10000,20000,40000,75000,125000,250000,500000,1000000]
        global liczba
        liczba += 1
        pieniadze_var.set("Twoje pieniądze: " + str(pieniadze[liczba]))
```


### sprawdz_przycisk_a(), sprawdz_przycisk_b(), sprawdz_przycisk_c(), sprawdz_przycisk_d():
Sprawdzają, czy odpowiedź jest poprawna, aktualizują pieniądze i przechodzą do kolejnego pytania.

przykład:

```
def sprawdz_przycisk_a():
    if (koncowy_tekst_poprawnej_odpowiedzi == odpowiedz_A):
        pieniadze_function()
        pytania()
        odp_a.config(state="active")
        odp_b.config(state="active")
        odp_c.config(state="active")
        odp_d.config(state="active")
    else:
        root.destroy()
```


### Telefonik():
Wyświetla informację o odpowiedzi przyjaciela.

przykład:

```
def Telefonik():
    messagebox.showinfo("Przyjaciel",f"Przyjaciel podpowiada, że {koncowy_tekst_poprawnej_odpowiedzi} to poprawna odpowiedź.")
    Telefon.config(state="disabled")
```


### PolNaPol_Funkcja():
Obsługuje mechanizm 50/50.

przykład:

```
def PolNaPol_Funkcja():
    if odpowiedz_A == koncowy_tekst_poprawnej_odpowiedzi:
        odp_c.config(state="disabled")
        odp_d.config(state="disabled")
```


### Publicznosc_Funkcja():
Obsługuje mechanizm "Publiczność".

przykład:

```
def Publicznosc_Funkcja():
    if odpowiedz_A == koncowy_tekst_poprawnej_odpowiedzi:
        wykres("A")
    if odpowiedz_B == koncowy_tekst_poprawnej_odpowiedzi:
        wykres("B")
    if odpowiedz_C == koncowy_tekst_poprawnej_odpowiedzi:
        wykres("C")
    if odpowiedz_D == koncowy_tekst_poprawnej_odpowiedzi:
        wykres("D")
```


### wykres(odp):
Tworzy wykres "Wynik publiczności".

przykład:

```
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
```



7.Autorzy
Baza danych, pomoc przy programowaniu - Krystian Tarnowski,

Funkcjonalność gry - Mateusz Cichosz,

Wygląd gry, pomoc przy programowaniu - Jan Gołębiowski,

Dokumentacja - Piotr Kowalewski.
