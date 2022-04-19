

s = raw_input()
t = raw_input()

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans)
