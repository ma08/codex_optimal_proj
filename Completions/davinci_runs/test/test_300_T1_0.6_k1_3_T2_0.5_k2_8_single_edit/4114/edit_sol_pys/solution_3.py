
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

x_sum = 0
y_sum = 0
h_sum = 0

for i in range(n):
    x_sum += arr[i][0]
    y_sum += arr[i][1]
    h_sum += arr[i][2]

cx = x_sum - arr[0][0] - arr[1][0] - arr[2][0]
cy = y_sum - arr[0][1] - arr[1][1] - arr[2][1]
h = h_sum - arr[0][2] - arr[1][2] - arr[2][2]

print(cx, cy, h)
