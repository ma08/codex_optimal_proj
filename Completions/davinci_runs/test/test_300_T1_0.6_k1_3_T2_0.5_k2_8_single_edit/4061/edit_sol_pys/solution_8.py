
s = input()  # abab
t = input()  # aba

cnt = 0

for i in range(len(s)):
    print(i)
    if s[i] == t[0]:
        cnt += 1
        t = t[1:]
        if len(t) == 0:
            break

if len(t) == 0:
    print(len(s) - cnt)
else:
    print(len(s))
