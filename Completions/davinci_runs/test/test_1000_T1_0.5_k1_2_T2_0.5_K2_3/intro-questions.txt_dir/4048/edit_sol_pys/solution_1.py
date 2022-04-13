n, m = map(int, input().split())
arr = [int(i) for i in input().split()]

for i in range(m):
    a, b, k = map(int, input().split())
    for j in range(a-1, b):
        arr[j] += k

print(max(arr))
