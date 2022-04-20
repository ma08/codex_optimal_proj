

s = input()
t = input()

s = list(s)
t = list(t)

sDict = {}
tDict = {}

for i in range(len(s)):
    sDict[s[i]] = s.count(s[i])
    tDict[t[i]] = t.count(t[i])

if sDict == tDict:
    print("Yes")
else:
    print("No")
