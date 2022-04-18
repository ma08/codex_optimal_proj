
# -----Answer-----
s = input()

def backspace(s):
    if len(s) == 0:
        return s
    return s[:-1]

for i in s:
    if i == 'B':
        s = backspace(s)
    else:
        s += i

print(s)
