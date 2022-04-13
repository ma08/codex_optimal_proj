n = int(input())
a = [0] * n
b = list(map(int, input().split()))
for i in range(1, n + 1):
    a[b[i-1] - 1] = i
print(' '.join(map(str, a)))
