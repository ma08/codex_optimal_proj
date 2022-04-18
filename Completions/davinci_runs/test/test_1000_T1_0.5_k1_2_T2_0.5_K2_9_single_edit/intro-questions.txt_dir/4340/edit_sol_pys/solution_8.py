

n = int(input())
a = [int(i) for i in input().split()]

for i in range(n):
    for j in range(i+1, n):
        if a[i] == a[j]:
            a[i] = -1
            a[j] = -1


b = []
for i in range(n):
    if a[i] != -1:
        b.append(a[i])

for i in range(len(b)):
    for j in range(i+1, len(b)):
        if b[i] == b[j]:
            b[i] = -1
            b[j] = -1

for i in range(len(b)):
    if b[i] != -1:
        print(b[i], end=' ')

for i in range(n):
    if a[i] == -1:
        print(a[i], end=' ')
