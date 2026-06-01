# blackjack
#
# uwagi:
#   - wartosc asa zle sie liczy
#       (istnieje sytacja w ktorej as liczy sie jako 11 a moze jako 1)

import random

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} {self.suit}"

    def __repr__(self):
        return self.__str__()

    def value(self, score):
        match self.rank:
            case 'As':
                if score > 10:
                    return 1
                else :
                    return 11
            case 'Król' | 'Dama' | 'Walet' :
                return 10
            case _:
                return int(self.rank)


class Deck:

    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Walet', 'Dama', 'Król', 'As']
        suits = ['Pik ♠', 'Kier ♥', 'Trefl ♣', 'Karo ♦']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def draw_random_card(self):
        if not self.cards:
            raise ValueError("Talia jest pusta! Nie można dobrać karty.")

        random_index = random.randrange(len(self.cards))

        return self.cards.pop(random_index)

    def count(self):
        return len(self.cards)


def draw(deck, who, score):
    drawn_card = deck.draw_random_card()

    match who:
        case "player":
            score["player"] += drawn_card.value(score["player"])
            print(f"GRACZ DOBIERA: {drawn_card}")
            print("WYNIK GRACZA: ", score["player"])

        case "croupier":
            score["croupier"] += drawn_card.value(score["croupier"])
            print(f"KRUPIER DOBIERA: {drawn_card}")
            print("WYNIK KRUPIERA: ", score["croupier"])


#gra z komputerem

if __name__ == "__main__":
    my_deck = Deck()
    score = {"player": 0, "croupier": 0}
    run = 'Y'

    draw(my_deck, "croupier", score)

    print("---TURA GRACZA---")

    draw(my_deck, "player", score)
    draw(my_deck, "player", score)

    if score["player"] == 21:
        print("wygrana!!!")
        quit()

    while run == 'Y':

        if score["player"] > 21:
            print("przegrana!!!")
            break

        run = input("---CZY CHCESZ DOBRAC KARTE? (Y/N)---").upper()

        if run == 'N':
            print("---TURA KRUPIERA---")
            while score["croupier"] < 17:
                draw(my_deck, "croupier", score)

            if score["croupier"] == score["player"]:
                print("remis!!!")
            elif score["player"] < score["croupier"] <= 21:
                print("przegrana!!!")
            else:
                print("wygrana!!!")

            break


        draw(my_deck, "player", score)


