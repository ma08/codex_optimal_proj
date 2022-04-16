

num_of_cards, shuffle = input().split()
num_of_cards = int(num_of_cards)

if shuffle == 'out':
    if num_of_cards % 2 == 0:
        print(num_of_cards // 2)
    else:
        print((num_of_cards // 2) + 1)
else:
    if num_of_cards % 2 == 0:
        print(num_of_cards // 2)
    else:
        print(num_of_cards // 2)
