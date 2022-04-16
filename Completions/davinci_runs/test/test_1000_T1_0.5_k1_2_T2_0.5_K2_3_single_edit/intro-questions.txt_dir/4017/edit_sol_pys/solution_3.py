n, m = map(int, input().split())
a = list(map(int, input().split()))


for i in range(m):
    l, r, x = map(int, input().split())
    for j in range(l-1, r):
        if a[j] < a[x-1]:
            print('Yes')
            break
    else:
        print('No')
