

s = input().strip()[::-1]
t = input().strip()[::-1]

for i in range(len(t)):
    if s[i] == t[i]:
        print('0', end='')
    else:
        print('1', end='')
