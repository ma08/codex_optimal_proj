

def missing_cards(s):
    cards = {'P': [], 'K': [], 'H': [], 'T': []}
    suits = ['P', 'K', 'H', 'T']
    for i in range(0, len(s), 3):
        cards[s[i]].append(s[i + 1:i + 3])
    for suit in suits:
        if len(cards[suit]) != 13:
            return 'GRESKA'  # GRESKA is a word in Serbian and means ERROR
        for card in cards[suit]:
            if cards[suit].count(card) > 1:
                return 'GRESKA'  # GRESKA is a word in Serbian and means ERROR
    return ' '.join([str(13 - len(cards[suit])) for suit in suits])  # ' '.join([str(13 - len(cards[suit])) for suit in suits])

print(missing_cards(input()))
