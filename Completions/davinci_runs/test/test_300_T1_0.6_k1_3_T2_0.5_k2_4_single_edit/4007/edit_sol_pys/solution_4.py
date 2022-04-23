

n = int(input())
f = list(map(int, input().split()))
f2 = [0] * n

for i in range(n):
    f2[f[i]-1] = i + 1
for i in range(n):
    for j in range(n):
        if f[j] == 0:
            f2[i] = j + 1
            break
for i in range(n):
    print(f2[i], end=' ')
