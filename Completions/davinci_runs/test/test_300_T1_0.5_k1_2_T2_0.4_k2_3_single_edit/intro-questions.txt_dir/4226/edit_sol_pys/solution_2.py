

# -----Answer-----
x, y = map(int, input().split())  # 入力

if y % 2 == 0:  # 偶数かどうか
    if (x * 2 + 4) / 2 == y:  # 式を書く
        print("Yes")
    else:
        print("No")
else:  # 偶数じゃないとき
    print("No")

# -----Other Answer-----
x, y = map(int, input().split())  # 入力

if x * 2 <= y <= x * 4:
    if y % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
