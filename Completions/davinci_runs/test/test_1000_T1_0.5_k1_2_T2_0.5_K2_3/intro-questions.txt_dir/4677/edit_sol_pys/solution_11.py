
def backspace(str):
    if len(str) == 0:
        return str
    else:
s = input()
        return str[:-1]

for i in s:
    if i == 'B':
        s = backspace(s)
    else:
        s += i

print(s)
