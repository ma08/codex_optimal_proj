

def check(cards, suits, numbers):

    for card in cards:
        suit = card[0]
        number = card[1:]
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

suits = {'P': 0, 'K': 0, 'H': 0, 'T': 0}
numbers = {'P': [], 'K': [], 'H': [], 'T': []}

check(input(), suits, numbers)
