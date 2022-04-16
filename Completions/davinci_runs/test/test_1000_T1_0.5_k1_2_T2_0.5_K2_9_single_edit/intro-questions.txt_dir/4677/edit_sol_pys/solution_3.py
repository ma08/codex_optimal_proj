
# -----Answer-----
s = input()

def backspace(str):
    if len(str) == 1:
        return str
    else:
        return str[:-2]

for i in s:
    if i == 'B':
        s = backspace(s)
        s = backspace(s)
    else:
        s = s + i

print(s)
