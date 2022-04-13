

n, shuffle = input().split() # n is number of cards, shuffle is type of shuffle
n = int(n) # convert string to int
if shuffle == 'out': # if shuffle is out
    if n % 2 == 0:
        print(n // 2)
    else:
        print((n // 2) + 1)
else:
    if n % 2 == 0:
        print(n // 2)
    else:
        print(n // 2)
