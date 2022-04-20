

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

k = int(input())

arr = sorted(arr, key=lambda x: x[k])

for i in arr:
    print(*i)
