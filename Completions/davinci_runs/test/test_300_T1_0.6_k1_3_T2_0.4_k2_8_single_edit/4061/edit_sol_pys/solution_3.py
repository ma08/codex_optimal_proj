s = input()
t = input()

cnt = 0

for i in range(len(s)):
    if s[i] == t[0]:
        cnt += 1
        t = t[1:]
    if not t:
        break

if not t:
    print(len(s) - cnt)
else:
    print(len(s))
