
s = input()
t = input()
corrects = 0
for i in range(len(s)):
    if s[i] == t[i]:
        corrects += 1
print(corrects)
