

n = int(input())
a = [int(x) for x in input().split()]

a.sort()

if n % 2 == 1:
    median = a[n//2]
else:
    median = (a[n//2] + a[n//2 - 1]) // 2

ans = 0
for x in a:
    ans += abs(x - median)
print(ans)