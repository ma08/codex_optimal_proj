

n = int(input())
a = list(map(int, input().split()))

maxs = [0] * n

for i in range(1, n):
    if a[i] <= 2 * a[i - 1]:
        maxs[i] = maxs[i - 1] + 1
    else:
        maxs[i] = maxs[i - 1]

print(maxs[-1] + 1)