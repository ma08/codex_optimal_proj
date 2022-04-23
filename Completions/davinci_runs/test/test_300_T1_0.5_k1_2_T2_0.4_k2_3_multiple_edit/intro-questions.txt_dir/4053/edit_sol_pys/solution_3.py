n = int(input())
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(n):
    b.append(input())
a = sorted(a, key=lambda x: len(x))
b = sorted(b, key=lambda x: len(x))
c = ''
for i in range(n):
    if a[i] == b[i]:
        c += 'P'
    else:
        c += 'S'
for i in range(n - 1, -1, -1):
    if a[i] == b[i]:
        c += 'P'
    else:
        c += 'S'
print(c)
