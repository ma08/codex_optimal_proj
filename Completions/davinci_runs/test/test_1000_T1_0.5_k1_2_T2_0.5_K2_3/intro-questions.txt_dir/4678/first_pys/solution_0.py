

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

stools = [0]
for i in range(n):
    if a[i] > stools[-1]:
        stools.append(a[i])
    else:
        stools[bisect_left(stools, a[i])] = a[i]
print(len(stools)-1)