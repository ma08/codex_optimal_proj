
def check(labels):
    suits = {'P': 0, 'K': 0, 'H': 0, 'T': 0, 'GRESKA': 0}
    numbers = {'P': [], 'K': [], 'H': [], 'T': [], 'GRESKA': []}

    for label in labels:
        suit = label[0]
        try:
            number = label[1:]
        except:
            suits['GRESKA'] += 1
            numbers['GRESKA'].append('GRESKA')
            continue
        suits[suit] += 1
        numbers[suit].append(number)

    for suit in suits:
        if suit != 'GRESKA':
            if suits[suit] != 13:
                print(13 - suits[suit], end=' ')
            else:
                if len(set(numbers[suit])) != 13:
                    print('GRESKA')
                    return
        else:
            if len(set(numbers[suit])) != 13:
                print('GRESKA')
                return
    print()

check(input())
