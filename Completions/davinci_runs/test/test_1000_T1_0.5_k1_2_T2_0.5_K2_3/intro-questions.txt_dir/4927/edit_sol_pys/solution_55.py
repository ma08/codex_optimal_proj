
#
n, m = map(int, input().split())

arr = [0] * n

for i in range(m):
    s, c = map(int, input().split())
    if arr[s - 1] == 0:
        arr[s - 1] = c
    elif arr[s - 1] != c:
        print(-1)
        exit()

if arr[0] == 0:
    arr[0] = 1

for i in range(1, n):
    if arr[i] == 0:
        arr[i] = 0

print(''.join(map(str, arr)))
