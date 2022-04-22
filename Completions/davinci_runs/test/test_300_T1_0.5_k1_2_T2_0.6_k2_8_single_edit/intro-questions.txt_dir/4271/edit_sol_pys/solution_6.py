def solve(n, d, p, b):
    ans = 0
    for i in range(n):
        ans += p[d[i] - 1]
        if i > 0 and d[i] == d[i - 1] + 1:
            ans += b[d[i - 1] - 1]


    return ans

ans = 0
for i in range(n):
    ans += points[dishes[i] - 1]
    if i > 0 and dishes[i] == dishes[i - 1] + 1:
        ans += bonus[dishes[i - 1] - 1]

print(ans)
