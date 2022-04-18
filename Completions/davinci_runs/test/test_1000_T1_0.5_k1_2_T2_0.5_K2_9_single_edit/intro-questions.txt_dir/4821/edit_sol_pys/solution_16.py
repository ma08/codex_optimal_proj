

def missing_cards(s):
    cards = {'P': set(), 'K': set(), 'H': set(), 'T': set()}
    suits = ['P', 'K', 'H', 'T']
    for i in range(0, len(s) - 1, 3):
        cards[s[i]].add(s[i + 1:i + 3])
    for suit in suits:
        if len(cards[suit]) != 13 or len(cards[suit]) != len(set(cards[suit])):
            return 'Greska'
    return ' '.join([str(13 - len(cards[suit])) for suit in suits])

print(missing_cards(input()))
