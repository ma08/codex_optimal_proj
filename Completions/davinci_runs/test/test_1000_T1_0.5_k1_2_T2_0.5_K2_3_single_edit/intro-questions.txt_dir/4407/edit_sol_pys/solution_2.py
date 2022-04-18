
n, q = map(int, input().split())
coins = list(map(int, input().split()))

for _ in range(q):
    a = int(input())
    res = 0
    for coin in coins:
        if a == coin:
            res += 1
            break
        elif a > coin:
            a -= coin
            res += 1 
    if a > 0:
        res = -1
    print(res)
