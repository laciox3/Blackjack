import blackjack
import stats
from inputimeout import inputimeout, TimeoutOccurred

import kasa
import historia

def oblicz_punkty(reka):
    punkty = 0
    asy = 0
    
    for karta in reka:
        wartosc = karta.Karta[1].value 
        
        if wartosc == 1:
            asy += 1
            punkty += 11 
        elif wartosc > 10:
            punkty += 10 
        else:
            punkty += wartosc 
            
    while punkty > 21 and asy > 0:
        punkty -= 10
        asy -= 1
        
    return punkty

def wyswietl_reke(nazwa, reka):
    karty_str = ", ".join([str(karta).strip() for karta in reka])
    punkty = oblicz_punkty(reka)
    print(f"{nazwa}: [{karty_str}] (Punkty: {punkty})")

def zagraj_partie():
    print("\n" + "="*30)
    print("        ROZDANIE KART")
    print("="*30)
    
    # INICJALIZACJA GRY
    il_talii=-1
    while(il_talii < 0 or il_talii > 8):
        il_talii = inputimeout(prompt="\nProszę podać na ile talii kart chcesz grać 1-8 talii (masz 15 sekund!): ", timeout=15.0).lower()
    gra = blackjack.Gra(il_talii)
    historia_gry = historia.HistoriaRuchow() #Inicjalizacja historii
    
    # ROZDANIE POCZĄTKOWE
    gra.losujgraczowi()
    gra.losujgraczowi()
    gra.losujkrupierowi()
    gra.losujkrupierowi()
    
    punkty_gracza = oblicz_punkty(gra.kartygracza)
    punkty_krupiera = oblicz_punkty(gra.kartykrupiera)
    
    if punkty_gracza == 21:
        wyswietl_reke("Twoje karty", gra.kartygracza)
        print("Karta krupiera: " + str(gra.kartykrupiera[0]).strip())
        
        print("\nBLACKJACK!")
        return 2 
    # ------------------------------------------------
    
    # TURA GRACZA
    while True:
        wyswietl_reke("Twoje karty", gra.kartygracza)
        
        pierwsza_karta_krupiera = str(gra.kartykrupiera[0]).strip()
        print(f"Karta krupiera: [{pierwsza_karta_krupiera}, ?????]")
        
        punkty_gracza = oblicz_punkty(gra.kartygracza)
        
        if punkty_gracza > 21:
            print("\nPrzekroczyłeś 21! Krupier wygrywa.")
            return -1
            
        if punkty_gracza == 21:
            print("\nMasz 21 punktów! Koniec dobierania.")
            break 

        try:
            #Dodano opcje [C] do zapytania
            decyzja = inputimeout(prompt="\nChcesz dobrać (D), pasować (P) czy COFNĄĆ (C)? [D/P/C] (masz 15 sekund!): ", timeout=15.0).lower()
        except TimeoutOccurred:
            print("\n\nCzas minął! Automatycznie pasujesz (P).")
            decyzja = 'p' 
    
        if decyzja == 'd':
            historia_gry.zapisz_stan() #Zapis historii przed dobraniem
            gra.losujgraczowi()
            print("-> Dobierasz kartę...\n")
        elif decyzja == 'c':
            historia_gry.cofnij(gra) #Cofnięcie
        elif decyzja == 'p':
            print("-> Pasujesz.\n")
            break 
        else:
            print("! Nieznana komenda. Wpisz 'D', 'P' lub 'C'.")

    # TURA KRUPIERA
    print("-" * 30)
    print("TURA KRUPIERA")
    print("-" * 30)
    
    punkty_krupiera = oblicz_punkty(gra.kartykrupiera)
    wyswietl_reke("Karty krupiera", gra.kartykrupiera)
    
    while punkty_krupiera < 17:
        print("-> Krupier dobiera kartę...")
        gra.losujkrupierowi()
        punkty_krupiera = oblicz_punkty(gra.kartykrupiera)
        wyswietl_reke("Karty krupiera", gra.kartykrupiera)

    # WYNIK KOŃCOWY
    print("\n" + "*"*30)
    print("            WYNIK")
    print("*"*30)
    
    punkty_gracza = oblicz_punkty(gra.kartygracza)
    
    if punkty_krupiera > 21:
        print("Krupier przekroczył 21! WYGRYWASZ!")
        return 1 
    elif punkty_gracza > punkty_krupiera:
        print(f"Wygrywasz! (Ty: {punkty_gracza} vs Krupier: {punkty_krupiera})")
        return 1 
    elif punkty_gracza < punkty_krupiera:
        print(f"Przegrywasz! (Ty: {punkty_gracza} vs Krupier: {punkty_krupiera})")
        return -1 
    else:
        print(f"Remis! Obaj macie {punkty_gracza} pkt.")
        return 0 

def main():
    print("Miłej zabawy przy grze w Blackjacka!")
    
    moje_staty = stats.wczytaj()
    stats.wyswietl(moje_staty)
    
    #Inicjalizacja portfela
    portfel = kasa.Kasa()
    portfel.zapytaj_o_poczatkowy_budzet()

    
    while True:
        #Pytanie o zakład
        stawka = portfel.pobierz_stawke()
        if stawka == 0:
            print("Koniec środków, koniec gry!")
            break

        wynik = zagraj_partie()
        
        if wynik == 1:
            moje_staty["wygrane"] += 1
        elif wynik == -1:
            moje_staty["przegrane"] += 1
        elif wynik == 0:
            moje_staty["remisy"] += 1
            
        stats.zapisz(moje_staty)
        
        #Rozliczenie finansowe
        portfel.rozlicz_gre(wynik, stawka)
        
        try:
            jeszcze_raz = inputimeout(prompt="\nCzy chcesz zagrać jeszcze jedną partię? tak/nie: [t]/[n](masz 15 sekund!): ", timeout=15.0).lower()
        except TimeoutOccurred:
            print("\n\nCzas minął! Automatycznie rezygnujesz z gry.")
            jeszcze_raz = 'n'

        if jeszcze_raz != 't':
            stats.wyswietl(moje_staty)
            print(f"\nDzięki za grę! Wychodzisz z kwotą: {portfel.saldo} PLN.") # <- Aktualizacja komunikatu
            input("\nNaciśnij Enter, aby zamknąć okno...") 
            break

if __name__ == "__main__":
    main()
