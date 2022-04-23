# Вариант 1

n = int(input())
a = [int(x) for x in input().split()]
b = a[n:]
c = []

for i in range(n):
    if a[i] in b:
        c.append(a[i])
    else:
        for j in range(n):
            if b[j] == a[i]:
                c.append(b[j])
                break

print(*c)

# Вариант 2
n = int(input())
a = [int(x) for x in input().split()]
b = a[n:]
c = []

for i in range(n):
    if a[i] in b:
        c.append(a[i])
    else:
        for j in range(n):
            if b[j] == a[i]:
                c.append(b[j])
                break

print(*c)
