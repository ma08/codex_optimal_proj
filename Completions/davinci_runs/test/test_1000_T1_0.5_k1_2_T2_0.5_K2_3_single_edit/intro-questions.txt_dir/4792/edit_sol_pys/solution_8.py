

s = input()
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        s = s[:i] + s[i+1:]
        i -= 1

print(s)
