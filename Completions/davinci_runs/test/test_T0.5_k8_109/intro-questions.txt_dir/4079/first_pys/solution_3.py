


def isDiverse(s):
    if len(s) == 1:
        return True
    if len(s) == 2:
        return abs(ord(s[0]) - ord(s[1])) == 1
    for i in range(len(s)-1):
        if abs(ord(s[i]) - ord(s[i+1])) != 1:
            return False
    return True


n = int(input())
for i in range(n):
    s = input()
    if isDiverse(s):
        print("Yes")
    else:
        print("No")