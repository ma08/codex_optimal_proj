s = input().strip()
t = input().strip()

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans)
