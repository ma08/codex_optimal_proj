# ----- Solution -----

t = int(input())

for i in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    count = 0
    for j in range(n):
        if a[j] % 3 == 0:
            count += 1
        if (a[j]+a[j+1]) % 3 == 0:
            count += 1
    print(count)
