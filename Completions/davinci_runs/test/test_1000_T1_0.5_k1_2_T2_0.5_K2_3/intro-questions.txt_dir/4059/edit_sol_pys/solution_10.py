
n = int(input())

ans = 0
for a in range(1, n):
    for b in range(1, n):
        c = n - a - b
        if c > 0 and a < b < c:
            ans += 1

print(ans)
