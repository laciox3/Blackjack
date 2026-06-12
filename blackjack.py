from enum import Enum
import random

class Kolor(Enum):
    PIK = 3
    KIER = 2
    KARO = 1
    TREFL = 0

class Liczba(Enum):
    AS = 1
    DWA = 2
    TRZY = 3
    CZTERY = 4
    PIEC = 5
    SZESC = 6
    SIEDEM = 7
    OSIEM = 8
    DZIEWIEC = 9
    DZIESIEC = 10
    WALET = 11
    KROLOWA = 12
    KROL = 13

class Karta:
    def __init__(self, kolor, liczba):
        self.Karta = (Kolor(kolor), Liczba(liczba))

    def __str__(self):
        res = ""
        match self.Karta[1]:
            case Liczba.AS: res += "as "
            case Liczba.DWA: res += "dwa "
            case Liczba.TRZY: res += "trzy "
            case Liczba.CZTERY: res += "cztery "
            case Liczba.PIEC: res += "piec "
            case Liczba.SZESC: res += "szesc "
            case Liczba.SIEDEM: res += "siedem "
            case Liczba.OSIEM:  res += "osiem "
            case Liczba.DZIEWIEC: res += "dziewiec "
            case Liczba.DZIESIEC: res += "dziesiec "
            case Liczba.WALET: res += "walet "
            case Liczba.KROLOWA: res += "krolowa "
            case Liczba.KROL: res += "krol "
        match self.Karta[0]:
            case Kolor.PIK: res += "pik"
            case Kolor.KIER: res += "kier"
            case Kolor.KARO: res += "karo"
            case Kolor.TREFL: res += "trefl"
        return res

    #tu edytując __str__ to robisz grafikę, proponuję tablicę strigów czy coś ale sie nie znam

class Talia:
    def __init__(self):
        self.talia=[Karta(i,j+1) for i in range (4) for j in range (13)]
        #talia 52 kart do gry

    def __str__(self):
        res=""
        for k in self.talia:
            res += str(k)
            res += " "
        return res
    #to nic nie robi dla gry

    def append(self, param):
        self.talia.append(param)


class Gra:
    def __init__(self, il):
        self.gra = ""
        #string gdzie wrzuca się co gracz zrobił
        self.talia = [Talia() for i in range (il)]
        #karty do losowania
        self.kartygracza = []
        #karty gracza
        self.ilgracza = 0
        self.kartykrupiera = []
        #karty typa
        self.ilkrupiera = 0


    def losujkrupierowi(self):
        tal = random.randint(0, len(self.talia)-1)
        kar = random.randint(0, len(self.talia[tal].talia)-1)
        self.kartykrupiera.append(self.talia[tal].talia[kar])
        self.talia[tal].talia.remove(self.talia[tal].talia[kar])
        self.ilkrupiera += 1

    def losujgraczowi(self):
        tal = random.randint(0, len(self.talia) - 1)
        kar = random.randint(0, len(self.talia[tal].talia) - 1)
        self.kartygracza.append(self.talia[tal].talia[kar])
        self.talia[tal].talia.remove(self.talia[tal].talia[kar])
        self.ilgracza += 1

    def cofnijkrupierowi(self):
        self.talia[random.randint(0,len(self.talia)-1)].append(self.kartykrupiera[self.ilkrupiera-1])
        self.kartykrupiera.remove(self.kartykrupiera[self.ilkrupiera-1])
        self.ilkrupiera -= 1

    def cofnijgraczowi(self):
        ostatnia_karta = self.kartygracza.pop()
        self.talia[random.randint(0, len(self.talia) - 1)].append(ostatnia_karta)
        self.ilgracza -= 1

#losuj___ losuje kartę i usuwa ją z talii, cofnij____ usuwa, przy za dużej ilości sie wywala czyli działa

