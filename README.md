Dokumentacja gry Milionerzy


## 1. Wprowadzenie

Aplikacja "Milionerzy" to program napisany w języku Python przy użyciu biblioteki Tkinter do interfejsu użytkownika. Aplikacja symuluje popularny telewizyjny quiz "Milionerzy", w którym gracze odpowiadają na serię pytań, aby zdobyć nagrody pieniężne.

## 2. Wymagania Systemowe

Aby uruchomić tę aplikację, potrzebujesz zainstalowanych następujących komponentów:

```
Python 3.x
Tkinter
mysql-connector-python
Matplotlib
NumPy
Pillow
```

Możesz też otworzyć terminal w folderze z grą i wpisać
```
pip install -r requirements.txt
```

## 3. Połączenie z Bazą Danych

Aplikacja łączy się z bazą danych MySQL przy użyciu biblioteki mysql.connector. Parametry połączenia są ustawiane na początku programu:

Host: localhost
Użytkownik: root
Hasło: [Brak hasła]
Baza danych: milionerzy


## 4. Zmienne

host - Zmienna przechowująca adres hosta, do którego nawiązywane jest połączenie z bazą danych MySQL. W Twoim przypadku ustawiona na "localhost".

user - Zmienna przechowująca nazwę użytkownika do bazy danych MySQL. W Twoim przypadku ustawiona na "root".

password - Zmienna przechowująca hasło użytkownika do bazy danych MySQL. W Twoim kodzie jest pusta, co oznacza brak hasła.

baza_danych - Zmienna przechowująca nazwę bazy danych, z którą nawiązywane jest połączenie. W Twoim przypadku ustawiona na "milionerzy".

connection - Zmienna reprezentująca połączenie z bazą danych MySQL. Tworzona jest za pomocą biblioteki mysql.connector i używa wcześniej zdefiniowanych danych, takich jak host, user, password, i baza_danych.

okno - Zmienna przechowująca wynik okna dialogowego, które pojawia się na początku aplikacji, pytając użytkownika, czy chce rozpocząć grę w Milionerów.

root - Zmienna reprezentująca główne okno interfejsu Tkinter. Tutaj jest tworzone okno główne gry.

pytanie_tekst - Zmienna typu StringVar przechowująca tekst pytania, który jest wyświetlany na ekranie.

PrzyciskOdp_A, PrzyciskOdp_B, PrzyciskOdp_C, PrzyciskOdp_D - Zmienne typu StringVar przechowujące tekst odpowiedzi A, B, C, D, które są wyświetlane na przyciskach w interfejsie.

pieniadze_var - Zmienna typu IntVar przechowująca aktualną wygraną gracza w grze.

telefon_var - Zmienna typu StringVar, która prawdopodobnie miała być używana w połączeniu z przyciskiem "Telefon do przyjaciela", ale nie jest wykorzystywana w Twoim kodzie.

uzyte - Lista, która przechowuje identyfikatory (ID) już użytych pytań. Resetowana jest przy ponownym rozpoczęciu gry.

losowe - Zmienna przechowująca losowo wybrane ID pytania.

zapytanie - Obiekt kursora do wykonywania komend SQL na połączeniu z bazą danych.

wynik, wynik_a, wynik_b, wynik_c, wynik_d, wynik_poprawna_odpowiedz - Zmienne przechowujące wyniki zapytań SQL, odpowiadające treści pytania, odpowiedziom A, B, C, D i poprawnej odpowiedzi.

tresc_pytania, tresc_odpowiedzi_a, tresc_odpowiedzi_b, tresc_odpowiedzi_c, tresc_odpowiedzi_d, tresc_poprawnej_odpowiedzi - Zmienne pomocnicze do przetwarzania wyników zapytań SQL, zawierające tekst bez znaków specjalnych.

odpowiedz_A, odpowiedz_B, odpowiedz_C, odpowiedz_D - Zmienne przechowujące treści odpowiedzi A, B, C i D.

koncowy_tekst_poprawnej_odpowiedzi - Zmienna przechowująca tekst poprawnej odpowiedzi na pytanie.

nrIndeks - Licznik, który śledzi aktualny indeks wygranej w grze.

pieniadze - Lista przechowująca kwoty wygranych w grze.

obraz - Obiekt obrazu (grafiki) wczytanego z pliku "do graficzki.gif".

tlo_obraz - Obiekt obrazu przekonwertowany na format ImageTk.PhotoImage do użycia jako tło w interfejsie Tkinter.

czcionka - Obiekt czcionki używanej w interfejsie Tkinter, ustawiona na czcionkę "Impact" o rozmiarze 20 punktów i wadze "bold".

image - Obiekt obrazu wczytanego z pliku "do graficzki.gif".

photo - Obiekt obrazu przekonwertowany na format ImageTk.PhotoImage, który jest używany jako tło w interfejsie Tkinter.

canvas - Obiekt Canvas w Tkinter, który jest używany do wyświetlania tła graficznego.

ramka_lewa, ramka_prawa, ramka_srodek, ramkanic - Obiekty ramki w Tkinter używane do układania elementów interfejsu.

pieniadze_wyswietl, pytanie_wyswietl, odpa_wyswietl, odpb_wyswietl, odpc_wyswietl, odpd_wyswietl, PolNaPol_wyswietl, Telefon_wyswietl, Publicznosc_wyswietl - Obiekty wyświetlające elementy interfejsu w oknie Canvas.

Spacja - Zmienna przechowująca pustą etykietę, używaną do oddzielania elementów w interfejsie.

Aplikacja losuje pytania z bazy danych i zapobiega ponownemu wybieraniu tych samych pytań w trakcie jednej gry. Pytania pobierane są z bazy danych na podstawie unikalnego ID pytania.


## 5. Funkcje

pytania() - Funkcja do pobierania i wyświetlania nowego pytania oraz jego odpowiedzi. Losuje pytanie z bazy danych, pobiera treść pytania i odpowiedzi, a następnie aktualizuje etykiety w interfejsie użytkownika.
```python
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

pieniadze_function() - Funkcja odpowiedzialna za zwiększanie wygranej gracza po udzieleniu poprawnej odpowiedzi. Zwiększa wartość zmiennej pieniadze_var i wykorzystuje ją do wyświetlenia aktualnej wygranej w interfejsie.

```python
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
``` 

AktywujPrzyciski() - Funkcja aktywująca przyciski odpowiedzi (A, B, C, D) po pobraniu nowego pytania. Umożliwia graczowi udzielanie odpowiedzi.

```python
def AktywujPrzyciski():
    odp_a.config(state="active")
    odp_b.config(state="active")
    odp_c.config(state="active")
    odp_d.config(state="active")
```

sprawdz_odpowiedz(odpowiedz) - Funkcja, która sprawdza, czy udzielona odpowiedź jest poprawna. Porównuje odpowiedź gracza z poprawną odpowiedzią pobraną z bazy danych. W przypadku błędnej odpowiedzi kończy grę lub wyświetla informację o wygranej.

```python
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
```


sprawdz_przycisk_a() - Funkcja wywoływana po wciśnięciu przycisku odpowiedzi A. Wywołuje sprawdz_odpowiedz(odpowiedz_A) w celu sprawdzenia odpowiedzi.

```python
def sprawdz_przycisk_a():
    sprawdz_odpowiedz(odpowiedz_A)
```

TelefonDoPrzyjaciela() - Funkcja wywoływana po wciśnięciu przycisku "Telefon do przyjaciela". Wyświetla informację o tym, jaką odpowiedź podpowiada przyjaciel.

```python
def TelefonDoPrzyjaciela():
    msg.showinfo("Przyjaciel",f"Przyjaciel podpowiada, że {koncowy_tekst_poprawnej_odpowiedzi} to poprawna odpowiedź.")
    Telefon.config(state="disabled")
```

PolNaPol_Funkcja() - Funkcja wywoływana po wciśnięciu przycisku "50/50". Usuwa dwie błędne odpowiedzi, pozostawiając jedną błędną i jedną poprawną odpowiedź.

```python
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
```

Publicznosc_Funkcja() - Funkcja wywoływana po wciśnięciu przycisku "Publiczność". Tworzy wykres przedstawiający procentową liczbę poparcia dla każdej odpowiedzi wśród publiczności.

```python
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

wykres(odp) - Funkcja generująca wykres "Wynik publiczności" na podstawie danych dotyczących wsparcia publiczności dla odpowiedzi A, B, C lub D. Wykres jest wyświetlany w osobnym oknie.

```python
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
```

## 6. Autorzy

Baza danych - Krystian Tarnowski
Funkcjonalność gry - Mateusz Cichosz
Wygląd gry - Jan Gołębiowski
Dokumentacja - Piotr Kowalewski



