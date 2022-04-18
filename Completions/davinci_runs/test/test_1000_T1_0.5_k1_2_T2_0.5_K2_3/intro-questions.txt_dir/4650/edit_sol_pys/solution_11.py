
# ----- Solution -----

#!/usr/bin/python3

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for j in range(n):
        if a[j] % 3 == 0:
            count += 1
    for j in range(n-1):
        if (a[j]+a[j+1]) % 3 == 0:
            count += 1
    print(count)
