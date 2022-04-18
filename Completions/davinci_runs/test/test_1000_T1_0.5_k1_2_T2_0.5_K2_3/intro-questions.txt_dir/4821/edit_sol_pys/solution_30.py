

def missing_cards(s):
    cards = {'P': [], 'K': [], 'H': [], 'T': []}  # cards[suit] = [card1, card2, ..., card13]
    suits = ['P', 'K', 'H', 'T']
    for i in range(0, len(s) - 1, 3):
        cards[s[i]].append(s[i + 1:i + 3])  # cards[suit].append(card)
    for suit in suits:
        if len(cards[suit]) != 13:  # if number of cards is not 13, then return error message
            return 'GRESKA'
        for card in cards[suit]:
            if cards[suit].count(card) > 1:  # if number of card is more than 1, then return error message
                return 'GRESKA'
    return ' '.join([str(13 - len(cards[suit])) for suit in suits])  # return number of missing cards for each suit

print(missing_cards(input()))
