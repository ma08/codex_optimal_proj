

def main():
    cards = [0]*52
    suits = {"C": 0, "D": 13, "H": 26, "S": 39, "N": 52}
    suit_names = ["C", "D", "H", "S", "N"]

    cards_input = input()
    for i in range(0, len(cards_input), 3):
        card = cards_input[i:i + 3]
        suit = suits[card[0]]
        number = int(card[1:]) - 1
        if cards[suit + number] == 1:
            print("GRESKA")
            return
        cards[suit + number] = 1

    for suit in suit_names:
        print(13 - sum(cards[suits[suit]:suits[suit] + 13]), end=" ")  # end=" " это для того, чтобы после последнего числа не было переноса строки


if __name__ == "__main__":
    main()
