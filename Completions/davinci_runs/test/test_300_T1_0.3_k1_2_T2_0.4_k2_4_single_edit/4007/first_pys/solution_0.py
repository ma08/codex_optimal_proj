

n = int(input())
f = list(map(int, input().split()))

for i in range(n):
    if f[i] == 0:
        for j in range(1, n+1):
            if j not in f:
                f[i] = j
                break

print(*f)