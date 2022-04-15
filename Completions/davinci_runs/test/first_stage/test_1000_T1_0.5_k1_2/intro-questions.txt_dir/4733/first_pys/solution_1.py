

n, shuffle = input().split()
n = int(n)

if shuffle == 'out':
    if n % 2 == 0:
        print(n // 2)
    else:
        print((n // 2) + 1)
else:
    if n % 2 == 0:
        print(n // 2)
    else:
        print(n // 2)