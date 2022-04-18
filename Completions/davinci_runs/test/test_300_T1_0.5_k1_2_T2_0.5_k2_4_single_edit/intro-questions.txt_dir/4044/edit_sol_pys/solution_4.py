
a, b, x = map(int, input().split())

s = '0' * a + '1' * b

for i in range(x):
    if i % 2 == 0:
        s = s[:i] + s[i+1] + s[i] + s[i+2:]
    else:
        s = s[:-i-1] + s[-i-2] + s[-i-1] + s[-i:]

print(''.join(s))
