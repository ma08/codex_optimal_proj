n, m = map(int, input().strip().split())
arr = [0] * n
for i in range(m):
    a, b, k = map(int, input().strip().split())
    for j in range(a - 1, b):
        arr[j] += k


print(max(arr))
