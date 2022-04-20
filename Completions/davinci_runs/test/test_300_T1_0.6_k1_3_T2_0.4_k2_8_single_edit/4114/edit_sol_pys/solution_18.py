n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cx = (arr[0][0] + arr[1][0] + arr[2][0] - arr[3][0]) // 2
cy = (arr[0][1] + arr[1][1] + arr[3][1] - arr[2][1]) // 2
h = arr[0][2] - abs(cx - arr[0][0]) - abs(cy - arr[0][1])
print(cx, cy, h)
