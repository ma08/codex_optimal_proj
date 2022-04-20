
n = int(input())
f = list(map(int, input().split()))
f2 = [0] * n

for i in range(n):
    if f[i] == 0:
        continue
    f2[f[i]-1] = i + 1
for i in range(n):
    if f2[i] != 0:
        print(f2[i], end = ' ')
        continue
    for j in range(n):
        if f[j] != f2[j]:
            f2[i] = j + 1
            f2[j] = i + 1
            break
    print(f2[i], end = ' ')
