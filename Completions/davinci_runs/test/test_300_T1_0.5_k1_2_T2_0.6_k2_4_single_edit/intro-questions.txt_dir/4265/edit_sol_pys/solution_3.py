

s = input() # AtCoder
t = input() # AtCoder

ans = 0 # 1
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans)
