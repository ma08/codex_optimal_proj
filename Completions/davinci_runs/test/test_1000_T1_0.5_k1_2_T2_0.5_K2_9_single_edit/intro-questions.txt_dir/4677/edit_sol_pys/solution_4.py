

# -----Answer-----

def backspace(s):
    return s[:-1]

for i in s:
    if i == 'B':
        s = backspace(s)
    else:
        s += i

print(s)
