
# -----Answer----- #
s = list(input())

def backspace(string):
    if len(string) == 0:
        return string
    else:
        return string[:-1]

for i in range(len(s)):
    if s[i] == 'B':
        s = backspace(s[:i]) + s[i+1:]
    else:
        s = s[:i] + s[i+1:]

print(''.join(s))
