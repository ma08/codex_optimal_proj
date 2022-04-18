from collections import defaultdict


def missing_cards(s):
    cards = defaultdict(list)
    suits = ['P', 'K', 'H', 'T']
    for i in range(0, len(s) - 1, 3):
        cards[s[i]].append(s[i + 1: i + 3])
    if len(cards['P']) != 13 or len(cards['K']) != 13 or len(cards['H']) != 13 or len(cards['T']) != 13:
        return 'GRESKA'
    return ' '.join([str(13 - len(cards[suit])) for suit in suits])


print(missing_cards(input()))
