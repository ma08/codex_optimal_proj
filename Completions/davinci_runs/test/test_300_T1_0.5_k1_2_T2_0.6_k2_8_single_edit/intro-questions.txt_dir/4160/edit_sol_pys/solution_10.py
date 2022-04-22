n = int(input())
a = [int(i) for i in input().split()]
for i in range(n - 1, -1, -1):
    print(a[i], end=' ')
