
a, b, c = [int(x) for x in input().split()]
s = input()
for i in range(len(s) - 1):
    if s[i] == 'A' and s[i + 1] == 'B':
        if a < b:
            a, b = b, a
    elif s[i] == 'A' and s[i + 1] == 'C':
        if a < c:
            a, c = c, a
    elif s[i] == 'B' and s[i + 1] == 'C':
        if b < c:
            b, c = c, b
print(a, b, c)
