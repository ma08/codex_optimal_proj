

def check(cards):
    suits = {'P': 0, 'K': 0, 'H': 0, 'T': 0}  # cards for each suit
    numbers = {'P': [], 'K': [], 'H': [], 'T': []}  # cards for each suit

    for card in cards:
        suit, number = card[0], card[1:]
        suits[suit] += 1
        numbers[suit].append(number)

    for suit in suits:

        if suits[suit] != 13:
            print(13 - suits[suit], end=' ')
        else:
            unique_numbers = set(numbers[suit])
            if len(unique_numbers) != 13:
                print('GRESKA')
                return
            else:
                print('GRESKA')
    print()

check(input().split())
