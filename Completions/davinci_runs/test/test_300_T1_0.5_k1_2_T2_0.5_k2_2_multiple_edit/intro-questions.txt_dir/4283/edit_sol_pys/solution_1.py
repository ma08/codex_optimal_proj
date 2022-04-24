n = int(input())
a = list(map(int, input().split()))
a.sort()

if n == 1:
    print(1)
    exit(0)
if a[-1] - a[0] <= 5:
    print(n)
else:
    i = 0
    j = 1
    count = 0
    while j < n:
        if a[j] - a[i] <= 5:
            j += 1
        else:
            i = j
            j += 1
        count = max(count, j - i)
    print(count)
