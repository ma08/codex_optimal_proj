
def main():
    cards = [0] * 52
    suits = {"P": 0, "K": 13, "H": 26, "T": 39}
    suit_names = ["P", "K", "H", "T"]

    cards_input = input()
    for i in range(0, len(cards_input), 3):
        card = cards_input[i:i + 3]
        suit = suits[card[0]]
        number = int(card[1:])
        if cards[suit + number - 1] == 1:
            print("GRESKA")
            return
        cards[suit + number - 1] = 1

    for suit in suit_names:
        print(13 - sum(cards[suits[suit]:suits[suit] + 13]), end=" ")


if __name__ == "__main__":
    main()
