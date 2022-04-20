

def diverse(s):
    s = list(s)
    s.sort()
    for i in range(0, len(s) - 1):
        if ord(s[i]) + 1 != ord(s[i+1]):
            return False
    return True

n = int(input())
for i in range(0, n):
    s = input()
    if diverse(s):
        print("Yes")
    else:
        print("No")