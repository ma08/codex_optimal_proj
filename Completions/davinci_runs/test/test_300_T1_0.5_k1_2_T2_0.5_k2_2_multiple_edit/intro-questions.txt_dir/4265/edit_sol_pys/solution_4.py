
s = input()
t = input()

ans = 0
for i in range(len(s)-1):
    if s[i] != t[i]:
        ans += 1

print(ans)
