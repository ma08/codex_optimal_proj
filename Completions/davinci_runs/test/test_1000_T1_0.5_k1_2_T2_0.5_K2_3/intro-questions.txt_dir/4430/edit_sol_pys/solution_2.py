n, m, k = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
ans = 0
for i in range(m):
    if k >= p[i]:
        k -= p[i]
        ans += 1
    else:
        break

print(ans)
