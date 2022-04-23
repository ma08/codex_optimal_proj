

n, m = map(int, input().split())  # n: 入力数, m: 入力数列の長さ
a = list(map(int, input().split()))  # a: 入力数列

a.sort()

if a[-1] > n:
    print(-1)
    exit()

s = 0
for i in range(m):
    s += a[i]

print(n - s)
