

a, b, x = map(int, input().split())

s = []
for i in range(a):
    s.append('0')
for i in range(b):
    s.append('1')

for i in range(x):  # i = 0, 1, 2
    if i % 2 == 0:  # i = 0, 2
        s[i], s[i+1] = s[i+1], s[i]  # s[0], s[1] = s[1], s[0], s[2], s[3] = s[3], s[2]
    else:
        s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

print(''.join(s))
