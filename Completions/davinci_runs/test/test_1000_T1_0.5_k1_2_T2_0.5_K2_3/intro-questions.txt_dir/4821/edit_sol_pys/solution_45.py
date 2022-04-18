
def check(cards):
    suits = {'P': 0, 'K': 0, 'H': 0, 'T': 0, 'A': 0}
    numbers = {'P': [], 'K': [], 'H': [], 'T': [], 'A': []}

    for card in cards:
        suit = card[0]
        number = card[1:]
        suits[suit] += 1
        numbers[suit].append(number)

    for suit in suits:
        if suits[suit] != 12:
            print(12 - suits[suit], end=' ')
        else:
            if len(set(numbers[suit])) != 12:
                print('GRESKA')
                return
    print()


while True:
    check(input())
