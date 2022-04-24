

s = input()
t = input()

s = list(s)
t = list(t)

sDict = {}
tDict = {}

for i in range(len(s)):
    sDict[s[i]] = 1
else:
    sDict[s[i]] += 1

    tDict[t[i]] = 1
else:
    tDict[t[i]] += 1

if sDict == tDict:
    print("Yes")
else:
    print("No")
