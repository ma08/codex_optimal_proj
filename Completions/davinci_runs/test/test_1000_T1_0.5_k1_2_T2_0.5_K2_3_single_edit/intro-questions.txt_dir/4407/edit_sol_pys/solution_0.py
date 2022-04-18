
n, q = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()

for _ in range(q):
    a = int(input())
    res = 0
    while a > 0:
        if a in coins:
            res += 1
            break
        elif a % 2 == 0 and a // 2 in coins:
            a = a // 2
            res += 1
        else:
            res = -1
            break
    print(res)
