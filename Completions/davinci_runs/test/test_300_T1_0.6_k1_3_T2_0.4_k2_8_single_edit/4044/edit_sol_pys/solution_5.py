
#!/usr/bin/env python

a, b, x = map(int, raw_input().split())
n = a + b
s = ''
for i in range(n):
    if (i < x):
        s += '0'
    else:
        s += '1'
print s
