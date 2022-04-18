

def missing_cards(cards):
    cards_dict = {'P': [], 'K': [], 'H': [], 'T': []}
    suits = ['P', 'K', 'H', 'T']
    for i in range(0, len(cards) - 1, 3):
        cards_dict[cards[i]].append(cards[i + 1:i + 3])
    for suit in suits:
        if len(cards_dict[suit]) != 13:
            return 'GRESKA'
        for card in cards_dict[suit]:
            if cards_dict[suit].count(card) > 1:
                return 'GRESKA'
    return ' '.join([str(13 - len(cards_dict[suit])) for suit in suits])

print(missing_cards(input()))
