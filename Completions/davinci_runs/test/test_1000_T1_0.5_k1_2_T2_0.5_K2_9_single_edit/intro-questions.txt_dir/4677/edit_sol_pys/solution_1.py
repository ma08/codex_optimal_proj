

# -----Answer-----
s = list(input())

def backspace(s):
    if len(s) == 0:
        return s
    else:
        return s[:-1]

for i in s:
    if i == "B":
        s.pop()
    else:
        s += i

print(*s, sep="")
