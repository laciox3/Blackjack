import blackjack

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
    print("       ROZDANIE KART")
    print("="*30)
    
    # INICJALIZACJA GRY
    gra = blackjack.Gra(4)
    
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
        return 
    # ------------------------------------------------
    
    # TURA GRACZA
    while True:
        wyswietl_reke("Twoje karty", gra.kartygracza)
        
        pierwsza_karta_krupiera = str(gra.kartykrupiera[0]).strip()
        print(f"Karta krupiera: [{pierwsza_karta_krupiera}, ?????]")
        
        punkty_gracza = oblicz_punkty(gra.kartygracza)
        
        if punkty_gracza > 21:
            print("\nPrzekroczyłeś 21! Krupier wygrywa.")
            return
            
        if punkty_gracza == 21:
            print("\nMasz 21 punktów! Koniec dobierania.")
            break 
            
        decyzja = input("\nChcesz dobrać kartę (D) czy pasować (P)? [D/P]: ").lower()
        
        if decyzja == 'd':
            gra.losujgraczowi()
            print("-> Dobierasz kartę...\n")
        elif decyzja == 'p':
            print("-> Pasujesz.\n")
            break
        else:
            print("! Nieznana komenda. Wpisz 'D' lub 'P'.")

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
    print("           WYNIK")
    print("*"*30)
    
    punkty_gracza = oblicz_punkty(gra.kartygracza)
    
    if punkty_krupiera > 21:
        print("Krupier przekroczył 21! WYGRYWASZ!")
    elif punkty_gracza > punkty_krupiera:
        print(f"Wygrywasz! (Ty: {punkty_gracza} vs Krupier: {punkty_krupiera})")
    elif punkty_gracza < punkty_krupiera:
        print(f"Przegrywasz! (Ty: {punkty_gracza} vs Krupier: {punkty_krupiera})")
    else:
        print(f"Remis! Obaj macie {punkty_gracza} pkt.")

def main():
    print("Miłej zabawy przy grze w Blackjacka!")
    
    while True:
        zagraj_partie()
        
        # Pytanie o kolejną grę
        jeszcze_raz = input("\nCzy chcesz zagrać kolejną partię? (T/N): ").lower()
        if jeszcze_raz != 't':
            print("\nDzięki za grę!")
            break

if __name__ == "__main__":
    main()