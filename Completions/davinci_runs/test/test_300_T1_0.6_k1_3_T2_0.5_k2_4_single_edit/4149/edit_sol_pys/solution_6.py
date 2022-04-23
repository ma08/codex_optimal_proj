

n = int(input())
b = [int(x) for x in input().split()]
a = []

for i in range(n):
    if b[i] in b[i+1:]:
        a.append(b[i])
    else:
        a.append(b[i])

print(*a)
