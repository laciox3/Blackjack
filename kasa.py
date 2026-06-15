class Kasa:
    def __init__(self):
        self.saldo = 0

    def zapytaj_o_poczatkowy_budzet(self):
        while True:
            try:
                kwota = int(input("\nIle masz początkowo pieniędzy do gry? PLN: "))
                if kwota > 0:
                    self.saldo = kwota
                    break
                else:
                    print("Podaj kwotę większą od zera.")
            except ValueError:
                print("To nie jest prawidłowa liczba.")

    def pobierz_stawke(self):
        if self.saldo <= 0:
            print("\nJesteś spłukany! Bankructwo.")
            return 0
            
        while True:
            try:
                stawka = int(input(f"\n[Twoje saldo: {self.saldo} PLN] Ile obstawiasz w tej rundzie? "))
                if 0 < stawka <= self.saldo:
                    return stawka
                else:
                    print(f"Możesz postawić od 1 do {self.saldo} PLN.")
            except ValueError:
                print("To nie jest prawidłowa liczba.")

    def rozlicz_gre(self, wynik, stawka):
        print("\n--- ROZLICZENIE FINANSOWE ---")
        if wynik == 1:
            self.saldo += stawka
            print(f"WYGRANA! Zyskujesz {stawka} PLN.")
        elif wynik == 2:
            self.saldo += (stawka*1.5)
            print("BLACKJACK! Zyskujesz ", stawka*1.5, " PLN.")
        elif wynik == -1:
            self.saldo -= stawka
            print(f"PRZEGRANA. Tracisz {stawka} PLN.")
        else:
            print(f"REMIS. Stawka {stawka} PLN wraca na Twoje konto.")
            
        print(f"Twoje aktualne saldo wynosi: {self.saldo} PLN")
        print("-----------------------------")
