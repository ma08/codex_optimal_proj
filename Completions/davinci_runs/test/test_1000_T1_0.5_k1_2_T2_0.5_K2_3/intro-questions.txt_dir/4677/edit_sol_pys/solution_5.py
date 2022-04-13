

# -----Answer----- 
s = input()

def backspace(str): # function to delete char at the end of string
    if len(str) == 0:
        return str
    else:
        return str[:-1]

for i in s:
    if i == 'B':
        s = backspace(s)
    else:
        s += i

print(s)
