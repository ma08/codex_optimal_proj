

# -----My Answer-----
x, y = map(int, input().split())  # 入力を2つに分けて整数に変換する

if y % 2 == 0:  # yが偶数のとき
    if (x * 2 + 4) / 2 == y:  # x*2+4がyと等しいとき
        print("Yes")
    else:
        print("No")
else:
    print("No")

# -----Other Answer-----
x, y = map(int, input().split())

if x * 2 <= y <= x * 4:
    if y % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
