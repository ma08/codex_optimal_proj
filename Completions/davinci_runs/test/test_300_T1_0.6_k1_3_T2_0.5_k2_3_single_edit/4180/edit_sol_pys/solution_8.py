

while True:
    N = int(input())

    if N < 1000:
        change = 1000 - (N % 1000)
        print(change)

    else:
        print(0)
