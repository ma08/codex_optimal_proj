

def check(labels):
    suits = {'P': 0, 'K': 0, 'H': 0, 'T': 0}
    # count of suits
    numbers = {'P': [], 'K': [], 'H': [], 'T': []}
    # list of numbers

    for label in labels:
        # count suits and numbers
        suit = label[0]
        # get suit
        number = label[1:]
        # get number
        suits[suit] += 1
        # count suit
        numbers[suit].append(number)
        # add number to list

    for suit in suits:
        # print missing cards
        if suits[suit] != 13:
            # if suit is missing
            print(13 - suits[suit], end=' ')
            # print number of missing cards
        else:
            # if suit is complete
            if len(set(numbers[suit])) != 13:
                # if there are duplicates
                print('GRESKA')
                print error
                return
                stop
    print()

# read input
check(input())
