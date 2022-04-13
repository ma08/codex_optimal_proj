
# Solution

n = int(input())
s = list(input())

if s[0] == s[1]:
    r = 1
    t = [s[0], 'R']
else:
    r = 0
    t = [s[0]]

for i in range(1, n - 1):
    if s[i] == s[i + 1]:
        r += 1
        if s[i] == 'R':
            t.append('G')
        elif s[i] == 'G':
            t.append('B')
        else:
            t.append('R')
    else:
        t.append(s[i])

t.append(s[-1])
print(r)
print(''.join(t))
