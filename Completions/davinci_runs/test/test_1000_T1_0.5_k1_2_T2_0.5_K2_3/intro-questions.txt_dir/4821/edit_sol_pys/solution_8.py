

def main():
    cards = [0] * 52 # 0 - 51
    suits = {"P": 0, "K": 13, "H": 26, "T": 39} # 0 - 12, 13 - 25, 26 - 38, 39 - 51
    suit_names = ["P", "K", "H", "T"] # P - 0, K - 1, H - 2, T - 3

    cards_input = input()
    for i in range(0, len(cards_input), 3): # i = 0, 3, 6, 9, ...
        card = cards_input[i:i+3]
        suit = suits[card[0]] # card[0] = P, K, H, T
        number = int(card[1:]) # card[1:] = 2, 3, 4, ...
        if cards[suit + number - 1] == 1: # card[0] = P, K, H, T
            print("GRESKA")
            return
        cards[suit + number - 1] = 1 # card[0] = P, K, H, T

    for suit in suit_names:
        print(13 - sum(cards[suits[suit]:suits[suit] + 13]), end=" ") # P - 0, K - 1, H - 2, T - 3

if __name__ == "__main__":
    main()
