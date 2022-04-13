

def missing_cards(cards):
    cards = {'P': [], 'K': [], 'H': [], 'T': []} # P - Pik, K - Karo, H - Herc, T - Tref
    suits = ['P', 'K', 'H', 'T']
    for i in range(0, len(cards) - 1, 3):
        cards[cards[i]].append(cards[i + 1:i + 3]) # dodaje karte u listu 
    for suit in suits:
        if len(cards[suit]) != 13: # ako ima vise od 13 karata u jednoj od boja, vraca GRESKA
            return 'GRESKA'
        for card in cards[suit]: # proverava da li ima duplikata u listi
            if cards[suit].count(card) > 1: # ako ima duplikata, vraca GRESKA
                return 'GRESKA'
    return ' '.join([str(13 - len(cards[suit])) for suit in suits]) # vraca razliku izmedju 13 i broj karata u odredjenoj boji

print(missing_cards(input()))
