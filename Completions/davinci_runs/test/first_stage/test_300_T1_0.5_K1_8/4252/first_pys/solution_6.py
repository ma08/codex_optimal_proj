

def removeX(s):
    s = s.replace("xxx","xx")
    if "xxx" in s:
        return removeX(s)
    else:
        return s

n = int(input())
s = input()

if "xxx" in s:
    print(len(s) - len(removeX(s)))
else:
    print(0)