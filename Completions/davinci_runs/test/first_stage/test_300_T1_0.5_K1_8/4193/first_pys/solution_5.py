

# 入力
bingo_card = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b_nums = [int(input()) for _ in range(N)]

# 各マスが選択されたかどうかを管理するリスト
selected_num = [[False for _ in range(3)] for _ in range(3)]

for b_num in b_nums:
    for i in range(3):
        for j in range(3):
            if bingo_card[i][j] == b_num:
                selected_num[i][j] = True
                break

# 横一列が選択されていればTrue
row_selected = any([all(selected_num[i]) for i in range(3)])
# 縦一列が選択されていればTrue
column_selected = any([all([selected_num[i][j] for i in range(3)]) for j in range(3)])
# 斜めが選択されていればTrue
diagonal_selected = all([selected_num[i][i] for i in range(3)]) or all([selected_num[i][2 - i] for i in range(3)])

# 横一列、縦一列、斜めが選択されていればBINGO
if row_selected or column_selected or diagonal_selected:
    print("Yes")
else:
    print("No")