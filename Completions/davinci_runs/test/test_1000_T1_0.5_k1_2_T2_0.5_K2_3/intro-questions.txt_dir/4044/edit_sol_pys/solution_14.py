a, b, x = map(int, input().split())

s = []
for i in range(a):
    s.append("0")
for i in range(b):
    s.append("1")

for i in range(x):
    s[i], s[-i-1] = s[-i-1], s[i]

print(''.join(s))
