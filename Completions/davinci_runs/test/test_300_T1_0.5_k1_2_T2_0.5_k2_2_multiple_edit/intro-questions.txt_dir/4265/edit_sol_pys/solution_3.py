s = input()
t = input()

ans = 0
for i in range(len(s) - 1):
    if s[i:i + 2] != t[i:i + 2]:
        ans += 1

print(ans)
