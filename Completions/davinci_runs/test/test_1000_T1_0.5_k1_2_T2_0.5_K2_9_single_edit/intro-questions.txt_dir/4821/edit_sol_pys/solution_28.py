def check(labels):
    suits = {'P': 0, 'K': 0, 'H': 0, 'T': 0, 'S': 0}
    numbers = {'P': [], 'K': [], 'H': [], 'T': [], 'S': []}


    for label in labels.split():
        suit = label[0]
        number = int(label[1:])
        suits[suit] += 1
        numbers[suit].append(number)

    for suit in suits.keys():
        if suits[suit] != 13 and suit != 'S':
            print(13 - suits[suit], end='', flush=True)
        else:
            if len(set(numbers[suit])) != 13:
                print('GRESKA')
                return
    print(end='\n')

check(input())
