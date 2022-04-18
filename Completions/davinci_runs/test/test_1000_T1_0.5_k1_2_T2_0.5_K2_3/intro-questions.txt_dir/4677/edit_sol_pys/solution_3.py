

# -----Answer-----
s = input()

def backspace(st): # function to delete char at the end of string
    if len(st) == 0:
        return st
    else:
        return st[:-1]

for i in s:
    if i == 'B':
        s = backspace(s)
    else:
        s += i

print(s)
