
a, b, x = map(int, input().split())

s = []
for i in range(a):
    s.append('0')
for i in range(b):
    s.append('1')

for i in range(x//2):
    s[i], s[i+1] = s[i+1], s[i]
    s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

if x % 2 == 1:
    s[x//2], s[x//2+1] = s[x//2+1], s[x//2]

print(''.join(s))
