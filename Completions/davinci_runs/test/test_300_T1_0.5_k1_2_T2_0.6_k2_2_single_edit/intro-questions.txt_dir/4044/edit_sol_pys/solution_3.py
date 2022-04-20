a, b, x = map(int, input().split())
s = '0' * a + '1' * b
for i in range(x):
    if i % 2 == 0:
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]


print(s)
