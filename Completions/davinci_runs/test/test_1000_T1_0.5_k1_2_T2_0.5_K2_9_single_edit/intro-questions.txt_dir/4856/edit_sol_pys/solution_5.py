

n = int(input())
a = input().split()
b = [int(i) for i in a]
b.sort()
c = []
for i in range(len(b)):
    if i != len(b) - 1:
        if b[i] != b[i + 1]:
            c.append(b[i])
    else:
        c.append(b[i])
for i in range(len(c)):
    print(c[i], end=' ')
