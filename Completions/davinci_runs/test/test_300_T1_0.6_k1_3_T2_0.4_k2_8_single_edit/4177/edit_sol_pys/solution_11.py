

s = input()

for i in range(len(s)):
    s = s[:i] + "*" + s[i+1:]
print(s)
