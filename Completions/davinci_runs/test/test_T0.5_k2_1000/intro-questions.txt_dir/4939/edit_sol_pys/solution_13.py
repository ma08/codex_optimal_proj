
n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(m):
    l, r, x = map(int, input().split())
    l -= 1
    r -= 1
    x -= 1

    if a[x] > 1:
        print('Yes')
    else:
        print('No')

    for j in range(l, r + 1):
        if a[j] > a[x]:
            a[j] -= 1
