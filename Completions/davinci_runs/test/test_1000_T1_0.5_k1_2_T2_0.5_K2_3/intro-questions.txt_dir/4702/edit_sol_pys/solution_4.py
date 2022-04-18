import math
n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(0, n):
    for j in range(i, n):
        for k in range(j, n):
            if (a[i] != a[j] and a[j] != a[k] and a[k] != a[i]):
                count += 1

print(count)
