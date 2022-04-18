

def missing_cards(s):
    cards = {'P': [], 'K': [], 'H': [], 'T': []}  # create dictionary of suits
    suits = ['P', 'K', 'H', 'T']  # create list of suits
    for i in range(0, len(s), 3):
        cards[s[i]].append(s[i + 1:i + 3])  # add card to the list of the suit
    for suit in suits:
        if len(cards[suit]) != 13:  # if there are less/more than 13 cards in suit
            return 'GRESKA'  # GRESKA is a word in Serbian and means ERROR
        for card in cards[suit]:
            if cards[suit].count(card) > 1:  # if there are more than 1 card with the same value in a suit
                return 'GRESKA'  # GRESKA is a word in Serbian and means ERROR
    return ' '.join([str(13 - len(cards[suit])) for suit in suits])  # return the number of missing cards for each suit

print(missing_cards(input()))
