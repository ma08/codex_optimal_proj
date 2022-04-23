
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
k = int(input())
tmp = [arr[i][k] for i in range(n)]
tmp.sort()
for i in range(n):
    arr[i].append(tmp[i])
arr.sort(key=lambda x: x[-1])
for i in range(n):
    print(*arr[i][:-1])
