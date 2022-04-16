
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
        else:
            for i in range(len(coins)):
                if a % coins[i] == 0:
                    a = a // coins[i]
                    res += 1
                    break
                else:
                    res = -1
                    break
    print(res)
