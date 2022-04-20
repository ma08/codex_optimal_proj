t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    min_price = a[0]
    bad_prices = 0
    for j in range(1, n):
        if a[j] < min_price:
            bad_prices += 1
        else:
            min_price = a[j]
    print(bad_prices)