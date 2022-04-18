
# -----Answer-----
s = input()

def backspace(str):
    if len(str) == 1:
        return str
    else:
        return str[:-1]
    if str[-1] == 'B':
        return backspace(str[:-1])
    return str[:-1]
    
while 'B' in s:
    s = backspace(s)
print(s)
