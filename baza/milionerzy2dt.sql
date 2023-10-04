-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 04 Paź 2023, 10:55
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
-- Baza danych: `milionerzy2dt`
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
(4, 'Jak nazywa się największy kontynent na Ziemi', 'Europa', 'Afryka', 'Azja', 'Ameryka Północna', 'Azja');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
