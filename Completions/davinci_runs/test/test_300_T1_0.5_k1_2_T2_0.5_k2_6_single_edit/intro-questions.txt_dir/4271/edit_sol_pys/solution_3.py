
s = input()
t = input()
s = '*' + s + '*'
t = '*' + t + '*'
c = 0
for i in range(len(s) - 1):
    if s[i] == t[i] and s[i + 1] == t[i + 1]:
        c += 1
print(c)
