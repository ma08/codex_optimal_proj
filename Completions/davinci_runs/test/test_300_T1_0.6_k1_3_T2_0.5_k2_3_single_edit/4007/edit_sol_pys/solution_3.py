

n = int(input())
f = list(map(int, input().split()))

f2 = [0] * n

for i in range(n):
    if f[i] == 0:
        continue
    f2[f[i]-1] = i + 1

print(*f2)
