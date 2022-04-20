

n = int(input())
a = list(map(int, input().split()))

b = [0] * n
for i in range(1, n - 1):
    if a[i - 1] == 1 and a[i + 1] == 1 and a[i] == 0:
        b[i - 1] += 1
        b[i] += 1
        b[i + 1] += 1

print(sum(b) // 2)