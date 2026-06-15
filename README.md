# 🃏 Blackjack – projekt grupowy

Konsolowa implementacja gry w Blackjacka napisana w Pythonie, stworzona w ramach przedmiotu **Narzędzia pracy grupowej**. Projekt obejmuje pełną logikę gry, system zarządzania talią kart, portfel gracza, zapisywanie statystyk oraz historię ruchów z możliwością cofania.

## 🎮 Funkcjonalności

- Implementacja gry od jednej do 8 tali 
- Gra z komputerem
- Statystyki wygranych zapamiętywane nawet po wyłączeniu programu
- Możliowość cofania ruchu
- Tryb gry na czas
- Gra z początkowym saldem

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

## 🛠️ Wykorzystane narzędzia pracy grupowej

- **Git/GitHub** – kontrola wersji, scalanie konfliktów
- Praca na osobnych gałęziach funkcjonalnych z późniejszym mergem do `main`
- **Discord** – komunikacja zespołowa
