

def check(cards):
    suits = {'P': 0, 'K': 0, 'H': 0, 'T': 0}
    numbers = {'P': [], 'K': [], 'H': [], 'T': []}

        if suit not in suits:
            print('GRESKA')
            return



        if number not in numbers[suit]:
            numbers[suit].append(number)
        else:
            print('GRESKA')
            return

    for card in cards:
        suit = card[0]
        number = card[1:]
        suits[suit] += 1

    for suit in suits:
        if suits[suit] != 13:
            print(13 - suits[suit], end=' ')
        else:
    print()

check(input())
