n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

x = (arr[0][0] + arr[1][0] + arr[2][0] - arr[3][0]) // 2
y = (arr[0][1] + arr[1][1] + arr[3][1] - arr[2][1]) // 2
h = arr[0][2] - abs(x - arr[0][0]) - abs(y - arr[0][1])
print(x, y, h)
