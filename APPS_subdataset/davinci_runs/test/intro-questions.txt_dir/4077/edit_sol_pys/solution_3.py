
n, m = map(int, input().split())
a = list(map(int, input().split()))

c = [0]*(2*10**5+1)
for i in range(n):
    c[a[i]] += 1

for i in range(1, len(c)):
    c[i] += c[i-1]

ans = 0
for i in range(n):
    ans += c[m] - c[a[i]]
    if a[i] == m:
        ans += 1

print(ans)
