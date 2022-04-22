
n = int(input())

ans = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if n - a * b > 0:
            ans += 1

print(ans)
