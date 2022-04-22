
n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n):
    if i == n-1:
        print(a[i])
    else:
        print(a[i], end=' ')
