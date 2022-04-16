n = int(input())
grid = [input() for _ in range(n)]  # 入力を行ごとにリストに格納


# 行をチェック
for row in grid:
    # 色の数をチェック
    if row.count('B') != row.count('W'):
        print(0)
        exit()
    # 連続する色をチェック
    for i in range(n-2):
        if row[i] == row[i+1] == row[i+2]:
            print(0)
            exit()

# 列をチェック
for j in range(n):
    column = [grid[i][j] for i in range(n)]  # 列を取り出す
    # 色の数をチェック
    if column.count('B') != column.count('W'):
        print(0)
        exit()
    # 連続する色をチェック
    for i in range(n-2):
        if column[i] == column[i+1] == column[i+2]:
            print(0)
            exit()

print(1)


# check row
for row in grid:
    # check color
    if row.count('B') != row.count('W'):
        print(0)
        exit()
    # check consecutive
    for i in range(n-2):
        if row[i] == row[i+1] == row[i+2]:
            print(0)
            exit()

# check column
for j in range(n):
    column = [grid[i][j] for i in range(n)]
    # check color
    if column.count('B') != column.count('W'):
        print(0)
        exit()
    # check consecutive
    for i in range(n-2):
        if column[i] == column[i+1] == column[i+2]:
            print(0)
            exit()

print(1)
