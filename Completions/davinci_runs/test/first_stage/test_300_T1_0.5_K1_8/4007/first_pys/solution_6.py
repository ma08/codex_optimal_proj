

n = int(input())
f = [int(x) for x in input().split()]

if f[0] == 0:
    for i in range(2,n+1):
        if i not in f:
            f[0] = i
            break

for i in range(1,n):
    if f[i] == 0:
        for j in range(1,n+1):
            if (j not in f) and (j != f[i-1]):
                f[i] = j
                break

print(*f)