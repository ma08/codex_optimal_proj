

s_raw = input()
t_raw = input()

s = s_raw
t = t_raw

counter = 0

while len(s) > 0 and len(t) > 0:
    if s[0] == t[0]:
        s = s[1:]
        t = t[1:]
    else:
        if s[0] == 'a':
            s = s[1:]
        else:
            t = t[1:]
        counter += 1

counter += len(s) + len(t)

print(counter)