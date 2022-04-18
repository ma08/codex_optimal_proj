

W, H, N = map(int, input().split())
x_y_a = [list(map(int, input().split())) for _ in range(N)]

x_min, x_max = 0, W
y_min, y_max = 0, H
for i in range(N):
    x = x_y_a[i][0]
    y = x_y_a[i][1]
    a = x_y_a[i][2]
    if a == 1:
        x_min = max(x_min, x)
    elif a == 2:
        x_max = min(x_max, x)
    elif a == 3:
        y_min = max(y_min, y)
    elif a == 4:
        y_max = min(y_max, y)

print((x_max - x_min) * (y_max - y_min))
