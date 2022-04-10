

n = int(input())
a = list(map(int, input().split()))

a.sort()

if n == 1:
    print(0)
    exit()

if (a[0] + a[-1]) % 2 == 0:
    print((a[0] + a[-1]) // 2)
else:
    print(-1)