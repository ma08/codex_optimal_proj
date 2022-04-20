

# 入力
n = int(input())
coordinate = []
for _ in range(n):
    x, y, h = map(int, input().split())
    coordinate.append([x, y, h])

# 四隅の座標を求める
min_x = coordinate[0][0]
min_y = coordinate[0][1]
max_x = coordinate[0][0]
max_y = coordinate[0][1]
for i in range(n):
    if coordinate[i][0] < min_x:
        min_x = coordinate[i][0]
    if coordinate[i][1] < min_y:
        min_y = coordinate[i][1]
    if coordinate[i][0] > max_x:
        max_x = coordinate[i][0]
    if coordinate[i][1] > max_y:
        max_y = coordinate[i][1]

# 中心座標を求める
c_x = 0
c_y = 0
h = 0
for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        for k in range(n):
            if coordinate[k][0] == i and coordinate[k][1] == j:
                curr_h = coordinate[k][2]
                break
            else:
                continue
        if max(h, curr_h - abs(i - coordinate[k][0]) - abs(j - coordinate[k][1])) > h:
            h = max(h, curr_h - abs(i - coordinate[k][0]) - abs(j - coordinate[k][1]))
            c_x = i
            c_y = j

# 出力
print(c_x, c_y, h)