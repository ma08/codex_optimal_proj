n, q = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()

for _ in range(q):
    a = int(input())
    res = 0
    for i in coins:
        if a <= 0:
            break
        a -= i
        res += 1
    if a > 0:
        res = -1
    print(res)
