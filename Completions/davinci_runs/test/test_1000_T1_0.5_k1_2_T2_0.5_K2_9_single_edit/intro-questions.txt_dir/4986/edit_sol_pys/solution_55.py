

s = input() # "abcd"
t = input() # "abcde"

result = "" # "e"

for i in range(len(s)):
    if s[i] != t[i]:
        result += s[i]

print(result)
