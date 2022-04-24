

s = input()
t = input()

def count(s):
    sDict = {}
    for i in s:
        if i not in sDict:
            sDict[i] = 1
        else:
            sDict[i] += 1
    return sDict

sDict = count(s)
tDict = count(t)

if sDict == tDict:
    print("Yes")
else:
    print("No")
