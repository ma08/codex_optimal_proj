

s = input()
t = input()

d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]].append(t[i])
    else:
        d[s[i]] = [t[i]]

for v in d.values():
    if len(set(v)) != 1:
        print("No")
        exit()
print("Yes")