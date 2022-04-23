
s = input()
d = 0
ans = 0

for i in range(len(s)):
    if i == 0:
        d = 1
    else:
        if s[i] == s[i-1]:
            d += 1
        else:
            ans += d//2
            d = 1

ans += d//2
print(ans)
