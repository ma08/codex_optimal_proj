

s = input()
t = input()

count = 0

while len(s) > 0 and len(t) > 0:
    if s[0] == t[0]:
        s = s[1:]
        t = t[1:]
    elif s[-1] == t[-1]:
        s = s[:-1]
        t = t[:-1]
    elif s[0] == t[-1]:
        s = s[1:]
        t = t[:-1]
    elif s[-1] == t[0]:
        s = s[:-1]
        t = t[1:]
    else:
        break

    count += 1

print(len(s)+len(t)+count*2)