

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
for i in range(m):
    if b[i] in a:
        ans += c[i]

print(x)
