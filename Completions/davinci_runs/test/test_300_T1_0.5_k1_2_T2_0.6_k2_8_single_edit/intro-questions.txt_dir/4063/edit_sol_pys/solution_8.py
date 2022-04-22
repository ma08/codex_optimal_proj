import math

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

cnt = 0
if a[0] == a[n - 1]:
    print(math.factorial(n) % (10 ** 9 + 7))
else:
    for i in range(n // 2):
        if a[i] == a[i + n // 2]:
            cnt += 1
        else:
            break
    print(math.factorial(n // 2 + cnt) % (10 ** 9 + 7))
