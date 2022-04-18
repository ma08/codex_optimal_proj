
def get_missing_cards(s):
    suit = {'P': [], 'K': [], 'H': [], 'T': []}
    for i in range(0, len(s), 3):
        suit[s[i]].append(s[i + 1:i + 3])
    return ' '.join([str(13 - len(suit[x])) for x in suit.keys()])
print(get_missing_cards(input()))
