

#Solution



n = int(input())
s = list(input())

if s[0] == s[1]:
    r = 1
    s[0] = 'R'
else:
    r = 0

for i in range(1, n - 1):
    if s[i] == s[i + 1]:
        r += 1
        if s[i] == 'R':
            s[i] = 'G'
        elif s[i] == 'G':
            s[i] = 'B'
        else:
            s[i] = 'R'

print(r)
print(''.join(s))
