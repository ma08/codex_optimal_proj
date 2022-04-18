
'''
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i] = int(input())
    for i in range(n):
        b[i] = int(input())
    for i in range(n):
        if a[i] != 0:
            b[a[i] - 1] = i + 1
    for i in range(n):
        print(b[i], end=' ')
'''

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

for i in range(n):
    if a[i] != 0:
        b[a[i] - 1] = i + 1

print(*b)
