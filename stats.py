import json
import os

PLIK_STATYSTYK = "statystyki.json"

def wczytaj():
    """Wczytuje statystyki z pliku JSON. Jeśli plik nie istnieje, wywala zera."""
    if os.path.exists(PLIK_STATYSTYK):
        with open(PLIK_STATYSTYK, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"wygrane": 0, "przegrane": 0, "remisy": 0}

def zapisz(staty):
    """Zapisuje statystyki po każdej grze."""
    with open(PLIK_STATYSTYK, "w", encoding="utf-8") as f:
        json.dump(staty, f, indent=4)

def wyswietl(staty):
    """Wylicza Win Ratio i pokazuje tablicę z wynikami."""
    wygrane = staty["wygrane"]
    przegrane = staty["przegrane"]
    remisy = staty["remisy"]
    
    rozegrane = wygrane + przegrane
    winratio = (wygrane / rozegrane * 100) if rozegrane > 0 else 0.0

    print("\n" + "="*30)
    print("      TWOJE STATYSTYKI")
    print("="*30)
    print(f" Wygrane:   {wygrane}")
    print(f" Przegrane: {przegrane}")
    print(f" Remisy:    {remisy}")
    print(f" Win Ratio: {winratio:.2f}%")
    print("="*30 + "\n")