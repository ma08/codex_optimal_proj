
n, a, b = map(int, input().split())
s = list(map(int, input().split()))
ans = 0
i = 0
while i < n:
    if a > 0:
        if s[i] == 1:
            a -= 1
            ans += 1
        else:
            ans += 1
    elif b > 0:
        b -= 1
        ans += 1
    else:
        break
    i += 1
print(ans)
