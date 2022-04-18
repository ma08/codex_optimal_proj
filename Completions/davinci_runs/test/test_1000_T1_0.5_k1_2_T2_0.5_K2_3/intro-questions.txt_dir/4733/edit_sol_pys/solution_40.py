

n, shuffle = input().split()  # n = number of cards, shuffle = type of shuffle
n = int(n)

if shuffle == 'out':
    if n % 2 == 0:
        print(n // 2)  # even number of cards
    else:
        print((n // 2) + 1)  # odd number of cards
else:
    if n % 2 == 0:
        print(n // 2)  # even number of cards
    else:
        print(n // 2)  # odd number of cards
