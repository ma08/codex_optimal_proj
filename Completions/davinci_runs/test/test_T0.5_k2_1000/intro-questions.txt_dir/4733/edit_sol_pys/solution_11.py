
n, shuffle = input().split()  # n = number of cards, shuffle = in or out
n = int(n)  # convert n to int

if shuffle == 'out':  # if shuffle is out
    print(n // 2)
else:
    print((n // 2) + 1)
