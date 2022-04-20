

s = input()
if len(s) % 2 == 0:
    for i in range(len(s)):
        s = s[:i] + "x" + s[i+1:]
    print(s)
else:
    for i in range(len(s)):
        s = s[:i] + "x" + s[i+1:]
    print(s)
