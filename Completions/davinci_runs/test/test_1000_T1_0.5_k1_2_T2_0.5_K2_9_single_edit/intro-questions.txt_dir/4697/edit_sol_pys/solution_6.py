

n, m = map(int, input().split())

ans = 0

if n == 0:
    ans = m // 3
    m %= 3
    ans += m
elif n == 1:
    ans = m // 3
    m %= 3
    ans += m
else:
    ans = m // 3
    m %= 3
    ans += m
    if n > m:
        ans += m
    else:
        ans += n
print(ans)
