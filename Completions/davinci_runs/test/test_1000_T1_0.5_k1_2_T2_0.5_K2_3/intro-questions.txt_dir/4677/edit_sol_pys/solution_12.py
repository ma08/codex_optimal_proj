

# -----Answer------
s = input()
s = list(s)
def backspace(str):
    return str[:-1]

for i in s:
    if i == 'B':
        s.pop()
    else:
        s.append(i)

print(''.join(s))
