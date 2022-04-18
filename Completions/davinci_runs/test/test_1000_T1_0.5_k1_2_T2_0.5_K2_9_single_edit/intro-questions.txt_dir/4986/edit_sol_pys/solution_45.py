

s = "abc"
t = "abc"

result = ''

for i in range(len(s)):
    if s[i] != t[i]:
        result += s[i] + ' '

print(result)
