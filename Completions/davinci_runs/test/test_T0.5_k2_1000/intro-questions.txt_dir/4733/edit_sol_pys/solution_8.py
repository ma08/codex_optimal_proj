

n, shuffle = input().split()  # take input
n = int(n)  # convert string to int

if shuffle == 'out':  # if shuffle is out
    if n % 2 == 0:
        print(n // 2)  # if n is even
    else:
        print((n // 2) + 1)  # if n is odd
else:  # if shuffle is in
    if n % 2 == 0:
        print(n // 2)  # if n is even
    else:
        print(n // 2)  # if n is odd
