

def check(hand):
    suits = {'P': 0, 'K': 0, 'H': 0, 'T': 0}
    numbers = {'P': [], 'K': [], 'H': [], 'T': []}

    for label in hand:
        suit = label[0]
        number = label[1:]
        suits[suit] += 1
        numbers[suit].append(number)

    for suit in suits:
        if suits[suit] != 13:
            print(13 - suits[suit], end=' ')
        else:
            if len(set(numbers[suit])) != 13:
                print('GRESKA')
                return
    print()

check(input())
