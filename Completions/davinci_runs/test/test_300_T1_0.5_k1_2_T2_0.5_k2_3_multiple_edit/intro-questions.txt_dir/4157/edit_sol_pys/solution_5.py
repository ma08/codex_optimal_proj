
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] % 3 == 0:
        a[i] //= 3
    else:
        a[i] *= 2
a.sort()
print(*a)
