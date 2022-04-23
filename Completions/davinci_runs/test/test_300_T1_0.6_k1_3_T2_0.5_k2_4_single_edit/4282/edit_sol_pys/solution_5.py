
def f(s):
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s
    if len(s) == 2:
        return s[1]+s[0]
    return s[len(s)-1] + f(s[1:len(s)-1]) + s[0]
print(f('abcde'))
