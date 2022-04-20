

n = int(input())
b = [int(x) for x in input().split()]
c = []
a = []

for i in range(n):
    for j in range(n, 2*n):
        if b[j] == b[i]:
            a.append(b[j])
            break

print(*a)
