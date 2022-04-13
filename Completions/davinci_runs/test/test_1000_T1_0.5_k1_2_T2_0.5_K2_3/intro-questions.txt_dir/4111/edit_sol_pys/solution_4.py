
a, b, c = map(int, input().split())
x, y = map(int, input().split())

ans = 0

if x <= y:
    if a + b > 2 * c:
        ans += min(x, y) * 2 * c
        x -= min(x, y)
        y -= min(x, y)
        ans += max(x, y) * min(a, 2 * c)
    else:
        ans += x * a
        y -= x
        ans += y * min(b, 2 * c)
else:
    if a + b > 2 * c:
        ans += min(x, y) * 2 * c
        x -= min(x, y)
        y -= min(x, y)
        ans += max(x, y) * min(b, 2 * c)
    else:
        ans += y * b
        x -= y
        ans += x * min(a, 2 * c)

print(ans)
