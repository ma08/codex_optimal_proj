n, m = map(int, input().split())
ans = 0

def calc(n, m):
    if n == 0:
        ans = m // 3
        m %= 3
        if m == 1:
            ans += 1
    elif n == 1:
        ans = m // 3
        m %= 3
        if m == 2:
            ans += 1
    else:
        ans = m // 3
        m %= 3
        if m == 1:
            ans += 1
        if n > m:
            ans += m
        else:
            ans += n
    return ans

ans = calc(n, m)

print(ans)
