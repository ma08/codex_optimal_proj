

def missing_cards(s):
    cards = {'C': [], 'D': [], 'H': [], 'S': []}
    suits = ['C', 'D', 'H', 'S']
    for i in range(0, len(s) - 1, 3):
        cards[s[i]].append(s[i + 1:i + 3])
    for suit in suits:
        if len(cards[suit]) != 13:
            return 'GRESKA'
        for card in cards[suit]:
            if cards[suit].count(card) > 1:
                return 'GRESKA'
    return ' '.join([str(13 - len(cards[suit])) for suit in suits])

print(missing_cards(input()))
