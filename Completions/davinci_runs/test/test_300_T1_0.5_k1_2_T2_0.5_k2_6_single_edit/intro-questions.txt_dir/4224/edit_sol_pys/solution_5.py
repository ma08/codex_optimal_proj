
n = int(input())
a = [int(x) for x in input().split()]

ans = 0

for i in range(n):
    while a[i] % 2 == 0:
        a[i] /= 2
        ans += 1

print(count)
