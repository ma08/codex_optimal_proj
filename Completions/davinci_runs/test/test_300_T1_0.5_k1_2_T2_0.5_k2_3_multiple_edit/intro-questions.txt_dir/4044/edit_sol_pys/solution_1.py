

a, b, x = map(int, input().split())  # a, b, x = 5, 5, 3

s = []  # s = []
for i in range(a):  # i = 0, 1, 2, 3, 4, 5
    s.append('0')  # s = ['0', '0', '0', '0', '0', '0']
for i in range(b):  # i = 0, 1, 2, 3, 4, 5
    s.append('1')  # s = ['0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1']

for i in range(x):  # i = 0, 1, 2, 3
    if i % 2 == 0:  # i = 0, 2
        s[i], s[i+1] = s[i+1], s[i]  # s[0], s[1] = s[1], s[0], s[2], s[3] = s[3], s[2], s[4], s[5] = s[5], s[4]
    else:
        s[-i-1], s[-i-2] = s[-i-2], s[-i-1]  # s[-1], s[-2] = s[-2], s[-1], s[-3], s[-4] = s[-4], s[-3]

print(''.join(s))
