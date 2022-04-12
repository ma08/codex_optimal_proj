

def main():
    cards = [0] * 52 # create a list of 52 zeroes
    suits = {"S": 0, "H": 13, "D": 26, "C": 39} # create a dictionary with suits
    suit_names = ["S", "H", "D", "C"] # create a list of suits

    cards_input = input() # get the input
    for i in range(0, len(cards_input), 3): # loop through the input
        card = cards_input[i:i+3] # get the card
        suit = suits[card[0]] # get the suit
        number = int(card[1:]) # get the number
        if cards[suit + number - 1] == 1: # check if the card is already in the list
            print("GRESKA")
            return # if the card is already in the list, print GRESKA and return
        cards[suit + number - 1] = 1 # if the card is not in the list, add it

    for suit in suit_names: # loop through the suits
        print(13 - sum(cards[suits[suit]:suits[suit] + 13]), end=" ") # print the number of missing cards

if __name__ == "__main__":
    main()
