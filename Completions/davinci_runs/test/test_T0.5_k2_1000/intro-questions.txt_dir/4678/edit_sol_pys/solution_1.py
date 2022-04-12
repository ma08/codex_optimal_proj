
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

stools = [0]  # stools[i] is the smallest height of a stool with i+1 stools
for i in range(n):
    if a[i] > stools[-1]:
        stools.append(a[i])
    else:
        stools[bisect_left(stools, a[i])] = a[i]
print(len(stools) - 1)
