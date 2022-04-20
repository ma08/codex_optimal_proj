

k = int(input())

if k % 7 == 0:
    print(1)
else:
    n = 0
    while True:
        n += 1
        if (10 ** n - 1) % k == 0:
            break
    print(n + 1)