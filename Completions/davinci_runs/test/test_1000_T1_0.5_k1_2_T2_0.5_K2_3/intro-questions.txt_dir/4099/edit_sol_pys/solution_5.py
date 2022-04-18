
n, m = map(int, input().split())
a = list(map(int, input().split()))

sumA = sum(a)
avg = sumA / n

if avg >= m:
    print(0)
    exit()

if m >= n:
    print(-1)
    exit()

print(m*n - sumA)
