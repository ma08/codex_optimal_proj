

s = input()[1:-1]
t = input()[1:-1]

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans)
