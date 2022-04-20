

# ==========
# 実装
# ==========
# 入力
sheet = []
for i in range(3):
    sheet.append(list(map(int, input().split())))

N = int(input())
bingo = []
for i in range(N):
    bingo.append(int(input()))

# ビンゴかどうか判定
for num in bingo:
    for i in range(3):
        for j in range(3):
            if num == sheet[i][j]:
                sheet[i][j] = 0

# 横、縦、斜めのどれかで0が3つ並んでいるか判定
if sheet[0][0] == 0 and sheet[0][1] == 0 and sheet[0][2] == 0:
    print("Yes")
elif sheet[1][0] == 0 and sheet[1][1] == 0 and sheet[1][2] == 0:
    print("Yes")
elif sheet[2][0] == 0 and sheet[2][1] == 0 and sheet[2][2] == 0:
    print("Yes")
elif sheet[0][0] == 0 and sheet[1][0] == 0 and sheet[2][0] == 0:
    print("Yes")
elif sheet[0][1] == 0 and sheet[1][1] == 0 and sheet[2][1] == 0:
    print("Yes")
elif sheet[0][2] == 0 and sheet[1][2] == 0 and sheet[2][2] == 0:
    print("Yes")
elif sheet[0][0] == 0 and sheet[1][1] == 0 and sheet[2][2] == 0:
    print("Yes")
elif sheet[0][2] == 0 and sheet[1][1] == 0 and sheet[2][0] == 0:
    print("Yes")
else:
    print("No")