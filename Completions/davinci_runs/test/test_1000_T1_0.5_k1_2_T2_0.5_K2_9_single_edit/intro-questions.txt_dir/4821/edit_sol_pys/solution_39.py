

def check_cards(s):
    cards = {'P': [], 'K': [], 'H': [], 'T': []} # create dictionary for suits
    suits = ['P', 'K', 'H', 'T'] # create list for suits
    for i in range(0, len(s) - 1, 3): # iterate over the string
        cards[s[i]].append(s[i + 1:i + 3]) # append to the dictionary
    for suit in suits: # iterate over the list
        if len(cards[suit]) != 13: # check if the length of the list is 13
            return 'GRESKA' # if it is not 13 return GRESKA
        for card in cards[suit]: # iterate over the list in the dictionary
            if cards[suit].count(card) > 1: # check if there is a duplicate
                return 'GRESKA' # if there is return GRESKA
    return ' '.join([str(13 - len(cards[suit])) for suit in suits]) # return the missing cards

print(missing_cards(input()))
