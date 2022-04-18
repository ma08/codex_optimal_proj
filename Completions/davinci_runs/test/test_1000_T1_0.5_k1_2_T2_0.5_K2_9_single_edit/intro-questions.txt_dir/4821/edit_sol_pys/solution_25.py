

def main():
    cards = [0] * 52 # create a list of 52 elements with value 0
    suits = {"P": 0, "K": 13, "H": 26, "T": 39} # dictionary of suits
    suit_names = ["P", "K", "H", "T"] # list of suit names

    cards_input = input() # input cards
    for i in range(0, len(cards_input), 3):
        card = cards_input[i:i+3]
        suit = suits[card[0]] # get suit
        number = int(card[1:]) # get number
        if cards[suit + number - 1] == 1: # if card is already in list
            print("GRESKA")
            return
        cards[suit + number - 1] = 1 # set card to 1

    for suit in suit_names:
        print(13 - sum(cards[suits[suit]:suits[suit] + 13]), end=" ") # print number of missing cards

if __name__ == "__main__":
    main()
