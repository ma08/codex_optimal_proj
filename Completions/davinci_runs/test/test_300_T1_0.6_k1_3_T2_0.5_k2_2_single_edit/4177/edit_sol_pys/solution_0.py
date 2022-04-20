
a = ""
s = input()

for i in range(len(s)):
    a += s[:i] + "x" + s[i+1:]
print(a)
