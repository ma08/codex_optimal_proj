
n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i):
        if a[j] > a[i]:
            a[j], a[i] = a[i], a[j]
    for k in range(n):
        print(a[k], end=' ')
    print('')
