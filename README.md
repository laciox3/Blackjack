# 🃏 Blackjack – projekt grupowy

Konsolowa implementacja gry w Blackjacka napisana w Pythonie, stworzona w ramach przedmiotu **Narzędzia pracy grupowej**. Projekt obejmuje pełną logikę gry, system zarządzania talią kart, portfel gracza, zapisywanie statystyk oraz historię ruchów z możliwością cofania.

## 🎮 Funkcjonalności

- Rozgrywka w Blackjacka z krupierem (sterowanym automatycznie)
- Liczenie punktów z uwzględnieniem asów (1/11)
- Automatyczna wygrana przy 21 punktach z dwóch pierwszych kart
- System zakładów i portfela gracza (saldo, stawki, rozliczenia)
- Zapisywanie statystyk (wygrane/przegrane/remisy, win ratio) do pliku JSON
- Limit czasu na decyzję gracza (timeout)
- Możliwość cofnięcia ostatniego dobrania karty

## 📁 Struktura plików

| Plik | Opis |
|---|---|
| `game.py` | Główna pętla gry, logika rozgrywki i punktacji |
| `blackjack.py` | Klasy `Karta`, `Talia`, `Gra` – reprezentacja kart i talii |
| `kasa.py` | Klasa `Kasa` – zarządzanie portfelem i zakładami gracza |
| `historia.py` | Klasa `HistoriaRuchow` – historia ruchów i mechanizm cofania |
| `stats.py` | Wczytywanie, zapis i wyświetlanie statystyk gracza |

## 🚀 Uruchomienie

```bash
pip install inputimeout
python game.py
```

## 👥 Historia rozwoju projektu

Projekt powstawał etapowo w ramach pracy zespołowej. Poniżej chronologiczny przebieg prac (od najstarszych commitów):

### Etap 1 – Fundamenty gry
- **PSroka** – dodanie pierwszych plików projektu
- **Jan** – podstawowe klasy gry oraz tryb gry z komputerem
- **Jan** – poprawka: automatyczna wygrana po uzyskaniu 21 punktów z dwóch pierwszych kart

### Etap 2 – Porządkowanie repozytorium
- **kkubbekk** – dodanie opisu projektu do README
- **Jan Stefanowicz** – aktualizacja README
- **Jan** – usunięcie kodu testowego z `main`
- **Jan Stefanowicz** – scalenie zmian porządkujących strukturę (PR #2, #3)
- **Jan Stefanowicz** – odwrócenie zmian restrukturyzacyjnych ("Revert Structure")

### Etap 3 – System portfela i historii ruchów
- **Jan Swed** – dodanie gry na pieniądze (klasa `Kasa`) oraz pamięci ruchów do cofania (klasa `HistoriaRuchow`)
- **Jan Stefanowicz** – scalenie odwrócenia zmian (PR #4)

### Etap 4 – Statystyki, gra z komputerem i finalizacja
- **Jan** – dodanie gry z komputerem
- **jakub s** – win ratio, zapis wyników do JSON oraz limit czasu na ruch
- **jakub s** – rozwiązanie konfliktu modify/delete – zachowanie plików gry
- **jakub s** – dodanie i naprawa pliku `.gitignore`

## 🛠️ Wykorzystane narzędzia pracy grupowej

- **Git/GitHub** – kontrola wersji, scalanie konfliktów
- Praca na osobnych gałęziach funkcjonalnych z późniejszym mergem do `main`

## 👨‍💻 Autorzy

- Jan Stefanowicz
- Jan Swed
- PSroka
- Jakub S.
