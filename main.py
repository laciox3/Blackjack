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


def gra_z_komputerem():
    """To jest w 100% oryginalny kod Twoich znajomych z głównej pętli."""
    my_deck = Deck()
    score = {"player": 0, "croupier": 0}
    run = 'Y'

    draw(my_deck, "croupier", score)

    print("---TURA GRACZA---")

    draw(my_deck, "player", score)
    draw(my_deck, "player", score)

    if score["player"] == 21:
        print("wygrana!!!")
        return

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


#PORTFEL

class Wallet:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance

    def get_bet(self):
        print(f"\nSTAN KONTA: {self.balance} PLN")
        while True:
            try:
                bet = int(input(f"Ile chcesz postawić? (1-{self.balance}): "))
                if 1 <= bet <= self.balance:
                    return bet
                print("Nieprawidłowa kwota! Nie masz tylu pieniędzy.")
            except ValueError:
                print("Podaj poprawną liczbę całkowitą!")

    def reward_win(self, bet):
        self.balance += bet
        print(f"Zyskujesz {bet} PLN.")

    def penalize_loss(self, bet):
        self.balance -= bet
        print(f"Tracisz {bet} PLN.")

    def is_bankrupt(self):
        return self.balance <= 0

#HISTORIA RUCHU

class GameHistory:
    def __init__(self):
        self.states = []

    def save_state(self, player_score, deck_cards):
        self.states.append({
            "player_score": player_score,
            "deck_cards": list(deck_cards)
        })

    def undo(self, score, deck):
        if not self.states:
            print("\n>>> Nie można cofnąć! Brak ruchów do cofnięcia.")
            return False
        
        last_state = self.states.pop()
        score["player"] = last_state["player_score"]
        deck.cards = last_state["deck_cards"]
        print(f"\n>>> COFNIĘTO RUCH! Twój wynik wraca do: {score['player']}")
        return True



#GRA NA PIENIĄDZE I Z COFANIEM

def gra_na_pieniadze():
    portfel = Wallet(1000)
    
    while not portfel.is_bankrupt():
        stawka = portfel.get_bet()
        my_deck = Deck()
        score = {"player": 0, "croupier": 0}
        historia = GameHistory()

        print("\n--- ROZDANIE POCZĄTKOWE ---")
        draw(my_deck, "croupier", score)
        print("\n--- TURA GRACZA ---")
        draw(my_deck, "player", score)
        draw(my_deck, "player", score)

        if score["player"] == 21:
            print("BLACKJACK! Wygrana!!!")
            portfel.reward_win(stawka)
            continue

        while True:
            if score["player"] > 21:
                print("Przekroczyłeś 21! Przegrana!!!")
                portfel.penalize_loss(stawka)
                break

            akcja = input("\n[Y] Dobierz | [N] Koniec tury | [C] Cofnij ruch: ").upper()

            if akcja == 'C':
                historia.undo(score, my_deck)
                continue
            elif akcja == 'Y':
                historia.save_state(score["player"], my_deck.cards)
                draw(my_deck, "player", score)
                continue
            elif akcja == 'N':
                print("\n--- TURA KRUPIERA ---")
                while score["croupier"] < 17:
                    draw(my_deck, "croupier", score)

                if score["croupier"] > 21:
                    print("Krupier przekroczył 21! Wygrana!!!")
                    portfel.reward_win(stawka)
                elif score["croupier"] == score["player"]:
                    print("Remis!!! Pieniądze wracają do portfela.")
                elif score["player"] < score["croupier"]:
                    print("Krupier ma więcej punktów. Przegrana!!!")
                    portfel.penalize_loss(stawka)
                else:
                    print("Masz więcej punktów. Wygrana!!!")
                    portfel.reward_win(stawka)
                break
        
        if portfel.is_bankrupt():
            print("\nZbankrutowałeś! Koniec gry.")
            break

        od_nowa = input("\nCzy chcesz zagrać kolejną rundę? (Y/N): ").upper()
        if od_nowa != 'Y':
            print(f"Dziękujemy za grę! Kończysz z kwotą {portfel.balance} PLN.")
            break


#MENU GŁÓWNE

def main():
    while True:
        print("\n" + "="*30)
        print("    WITAJ W BLACKJACKU")
        print("="*30)
        print("1. Klasyczna gra z komputerem (Trening)")
        print("2. Gra na pieniądze z opcją cofania ruchu")
        print("3. Wyjście z programu")
        print("="*30)
        
        wybor = input("Wybierz tryb (1/2/3): ")
        
        if wybor == '1':
            print("\nUruchamiam: Klasyczna gra z komputerem...\n")
            gra_z_komputerem()
        elif wybor == '2':
            print("\nUruchamiam: Gra na pieniądze...\n")
            gra_na_pieniadze()
        elif wybor == '3':
            print("Do zobaczenia!")
            break
        else:
            print("Niepoprawny wybór. Wybierz 1, 2 lub 3.")

if __name__ == "__main__":
    main()

