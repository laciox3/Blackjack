class HistoriaRuchow:
    def __init__(self):
        self.stos = []

    def zapisz_stan(self):
        self.stos.append("DOBRANIE")

    def cofnij(self, gra):
        if not self.stos:
            print("\n>>> Nie możesz cofnąć! Brak ruchów w historii.")
            return False
            
        ostatni_ruch = self.stos.pop()
        if ostatni_ruch == "DOBRANIE":
            gra.cofnijgraczowi()
            print("\n>>> COFNIĘTO RUCH! Karta wróciła do talii.")
            return True
        return False