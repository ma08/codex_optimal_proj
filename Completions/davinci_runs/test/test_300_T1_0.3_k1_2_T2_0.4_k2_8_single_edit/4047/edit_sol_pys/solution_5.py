def solve(n, x):
    x.sort()


    ans = 0
    for i in range(1, n):
        if x[i] - x[i-1] > 1:
            ans += x[i] - x[i-1] - 1

x.sort()

ans = 0
for i in range(1, n):
    if x[i] - x[i-1] > 1:
        ans += x[i] - x[i-1] - 1

print(ans)
