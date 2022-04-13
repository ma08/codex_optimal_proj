
n, q = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()

for _ in range(q):
    a = int(input())
    res = 0
    while a > 0:
        if a % 2 == 0:
            a = a // 2
            res += 1
        elif a in coins:
            res += 1
            break
        else:
            res = -1
            break
    print(res)
