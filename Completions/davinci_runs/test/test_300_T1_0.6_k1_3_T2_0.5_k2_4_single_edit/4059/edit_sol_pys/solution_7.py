

N = int(input())

ans = 0

for a in range(1, N + 1):
    b = (N - a)
    if b > 0:
        c = (N - a - b)
        if c > 0:
            ans += 1

print(ans)
