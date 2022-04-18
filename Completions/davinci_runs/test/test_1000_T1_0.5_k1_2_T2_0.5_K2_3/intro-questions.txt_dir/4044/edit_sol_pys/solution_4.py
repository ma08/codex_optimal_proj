
A, B, X = map(int, input().split())

s = []
for i in range(A):
    s.append('0')
for i in range(B):
    s.append('1')

for i in range(X):
    if i % 2 == 0:
        s[i], s[i+1] = s[i+1], s[i]
    else:
        s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

print(''.join(s))
