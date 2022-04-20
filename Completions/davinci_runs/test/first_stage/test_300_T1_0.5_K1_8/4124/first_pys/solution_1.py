

s = input()
t = input()

if len(s) > len(t):
    s, t = t, s

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans + len(t) - len(s))