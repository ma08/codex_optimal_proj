from itertools import combinations

n, w = map(int, input().split())
a = list(map(int, input().split()))

i = j = 0

if max(a) > w or min(a) < -w:
    print(0)
else:
    for i in range(n):
        j += a[i]
        if j > w or j < 0:
            print(0)
            break

    if i == n-1:

        print(w-j+1)
