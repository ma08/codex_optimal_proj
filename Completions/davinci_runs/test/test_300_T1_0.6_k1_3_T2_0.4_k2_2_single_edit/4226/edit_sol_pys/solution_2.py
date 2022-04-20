
A, B, C, X, Y = map(int, input().split())
ans = 10 ** 9
for i in range(10 ** 5 + 1):
    tmp = A * max(0, X - i) + B * max(0, Y - i) + 2 * C * i
    ans = min(ans, tmp)
print(ans)
