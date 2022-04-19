
s = input()
t = input()

ans = 0
for i in range(len(s)):  # i = 0, 1, 2, 3, 4
    if s[i] != t[i]:  # s[0] != t[0]
        ans += 1

print(ans)
