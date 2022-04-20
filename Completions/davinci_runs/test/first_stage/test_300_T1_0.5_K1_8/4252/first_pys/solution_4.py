

n = int(input())
s = input()

def remove_x(s):
    if "xxx" not in s:
        return 0
    else:
        if s[0] == "x":
            return 1 + remove_x(s[1:])
        elif s[-1] == "x":
            return 1 + remove_x(s[:-1])
        else:
            return 1 + min(remove_x(s[:-1]), remove_x(s[1:]))

print(remove_x(s))