
s = input()  # s = abracadabra
t = input()  # t = abra

cnt = 0

for i in range(len(s)):
    if s[i] == t[0]:  # s[i] = a, b, r, a, c, a, d, a, b, r, a
        # t[0] = a, b, r, a
        cnt += 1
        t = t[1:]
    if len(t) == 0:
        break

if len(t) == 0:
    print(len(s) - cnt)
else:
    print(len(s))
