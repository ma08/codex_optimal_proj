
s = input()
t = input()
 
result = ""

for i in range(len(s)):
    if s[i] != t[i]:
        result += s[i]

print(result)
