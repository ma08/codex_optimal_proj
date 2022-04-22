
s = input() # a,b,c
t = input() # d,e,f

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans)
