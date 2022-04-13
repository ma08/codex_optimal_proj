

def missing_cards(deck):
    cards = {'P': [], 'K': [], 'H': [], 'T': []} # P = Pikovi, K = Kockice, H = Herc, T = Tref
    suits = ['P', 'K', 'H', 'T']
    for i in range(0, len(cards) - 1, 3):
        cards[cards[i]].append(cards[i + 1:i + 3])
    for suit in suits:
        if len(cards[suit]) != 13:
            return 'GRESKA'
        for card in cards[suit]:
            if cards[suit].count(card) > 1:
                return 'GRESKA'
    return ' '.join([str(13 - len(cards[suit])) for suit in suits])

print(missing_cards(input()))
