
s = input()

def backspace(string):
    if len(string) == 0:
        return string
    else:
        return string[:-1]

for i in s:
    if i == 'B':
        s = backspace(s)
    else:
        s += i

print(s)
