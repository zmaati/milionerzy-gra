-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 04 Paź 2023, 11:36
-- Wersja serwera: 10.4.25-MariaDB
-- Wersja PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `milionerzy`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pytania`
--

CREATE TABLE `pytania` (
  `id` int(11) NOT NULL,
  `tresc` text NOT NULL,
  `odp_a` text NOT NULL,
  `odp_b` text NOT NULL,
  `odp_c` text NOT NULL,
  `odp_d` text NOT NULL,
  `pop_odp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pytania`
--

INSERT INTO `pytania` (`id`, `tresc`, `odp_a`, `odp_b`, `odp_c`, `odp_d`, `pop_odp`) VALUES
(1, 'Kto napisał \"Romeo i Julia\"?', 'Charles Dickens', 'William Shakespeare', 'Jane Austen', 'Leo Tolstoj', 'William Shakespeare'),
(2, 'Ile wynosi pierwiastek kwadratowy z 144?', '10', '12', '14', '16', '12'),
(3, 'Które zwierzę jest symbolizowane przez chiński znak zodiaku \"rok szczura\"?', 'Koń', 'Tygrys', 'Smok', 'Szczur', 'Szczur'),
(4, 'Jak nazywa się największy kontynent na Ziemi', 'Europa', 'Afryka', 'Azja', 'Ameryka Północna', 'Azja'),
(5, 'Która planeta jest znana jako \"Planeta Czerwona\"?', 'Wenus', 'Mars', 'Jowisz', 'Saturn', 'Mars'),
(6, 'Ile wynosi 7*8?', '15', '56', '64', '76', '56'),
(7, 'W którym roku miała miejsce pierwsza misja na Księżycu?', '1961', '1969', '1975', '1983', '1969'),
(8, 'Jaki jest skrót krajowy Stanów Zjednoczonych?', 'UK', 'USA', 'UAE', 'USB', 'USA'),
(9, 'Jakie jest główne paliwo rakietowe używane do wznoszenia wahadłowców w kosmos?', 'Benzyna', 'Diesel', 'Kerosen', 'Paliwo rakietowe', 'Kerosen'),
(10, 'Kto jest autorem \"Makbeta\"?', 'George Orwell', 'Mark Twain', 'William Shakespeare', 'Edgar Allan Poe', 'William Shakespeare'),
(11, 'Ile wynosi suma miar wszystkich kątów w trójkącie?', '90 stopni', '120 stopni', '180 stopni', '360 stopni', '180 stopni'),
(12, 'Kto jest autorem książki \"Zabić drozda\"?', 'J.K. Rowling', 'George Orwell', 'Harper Lee', 'Charles Dickens', 'Harper Lee'),
(13, 'Które zwierzę z rodziny niedźwiedziowatych jest czarno-białe i zagrożone wyginięciem?', 'Panda', 'Koala', 'Orangutan', 'Tygrys', 'Panda'),
(14, 'Która rzeka jest najdłuższą na świecie?', 'Nil', 'Amazonka', 'Missouri', 'Jangcy', 'Nil'),
(15, 'Która planeta jest najbliższa Słońcu?', 'Mars', 'Wenus', 'Saturn', 'Uran', 'Wenus'),
(16, 'Ile kontynentów jest na Ziemi?', '5', '6', '7', '8', '7'),
(17, 'W którym roku wybuchła I wojna światowa?', '1901', '1914', '1923', '1939', '1914'),
(18, 'Które państwo jest znane jako \"Kraj kwitnącej wiśni\"?', 'Chiny', 'Rosja', 'Japonia', 'Indie', 'Japonia'),
(19, 'Która nazwa gry spośród podanych to planszówka z literkami i planszą do tworzenia słów?', 'Scrabble', 'Monopoly', 'Chess', 'Risk', 'Scrabble'),
(20, 'Ile wynosi 2 do potęgi 5?', '4', '8', '16', '32', '32'),
(21, 'Gdzie znajduje się \"Wielki Mur\"?', 'We Francji', 'W Wielkiej Brytani', 'W Singapurze', 'W Chinach', 'W Chinach'),
(22, 'Która z planet jest największa w układzie słonecznym?', 'Mars', 'Wenus', 'Saturn', 'Jowisz', 'Jowisz'),
(23, 'Kto jest autorem powieści \"Zbrodnia i kara\"?', 'Fiodor Dostojewski', 'Leo Tolstoj', 'James Joyce', 'Charles Dickens', 'Fiodor Dostojewski'),
(24, 'Które państwo jest najmniejsze pod względem powierzchni na świecie?', 'Rosja', 'Monako', 'San Marino', 'Watykan', 'Watykan'),
(25, 'Jak nazywa się najwyższa góra na świeie?', 'Mont Blanc', 'Kilimandżaro', 'Mount Everest', 'K2', 'Mount Everest'),
(26, 'Która z opcji to najważniejszy składnik powietrza, którym oddychamy?', 'Tlen', 'Azot', 'Wodór', 'Dwutlenek Węgla', 'Tlen'),
(27, 'Które państwo jest najbardziej znane z produkcji wina?', 'Francja', 'Włochy', 'Hiszpania', 'Portugalia', 'Włochy'),
(28, 'Które miasto jest stolica Francji?', 'Berlin', 'Warszawa', 'Amsterdam', 'Paryż', 'Paryż'),
(29, 'Jak nazywa się biały proszek stosowany jako substancja słodka?', 'Cukier', 'Sól', 'Mąka', 'Kofeina', 'Cukier'),
(30, 'Jak nazywa się substancja chemiczna, która nadaje kolor liściom roślin?', 'Kofeina', 'Chlorofil', 'Kwas mlekowy', 'Wapń', 'Chlorofil'),
(31, 'Jaki jest największy ocean na Ziemi?', 'Ocean Atlantycki', 'Ocean Indyjski', 'Ocean Arktyczny', 'Ocean Spokojny', 'Ocean Spokojny'),
(32, 'Który pierwiastek jest znany jako \"pierwiastek szlachetny\"?', 'Azot', 'Hel', 'Wodór', 'Węgiel', 'Hel'),
(33, 'Ile dni ma luty w roku przestępnym.', '27', '28', '29', '30', '29'),
(34, 'Które miasto jest stolica Australii?', 'Melbourne', 'Canberra', 'Perth', 'Sydney', 'Canberra'),
(35, 'Jak nazywa się substancja chemiczna, która nadaje czerwoną barwę krwi?', 'Hemoglobina', 'Melanina', 'Kolagen', 'Insulina', 'Hemoglobina');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `pytania`
--
ALTER TABLE `pytania`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `pytania`
--
ALTER TABLE `pytania`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
