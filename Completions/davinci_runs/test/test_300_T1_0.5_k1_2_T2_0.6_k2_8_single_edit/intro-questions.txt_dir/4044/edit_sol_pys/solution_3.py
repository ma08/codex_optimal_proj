

a, b, x = map(int, input().split())  # put a, b, x into a list

s = []
for i in range(a):
    s.append('0')  # append a's 0s to s
for i in range(b):
    s.append('1')  # append b's 1s to s

for i in range(x):
    if i % 2 == 0:
        s[i], s[i+1] = s[i+1], s[i]
    else:
        s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

print(''.join(s))
