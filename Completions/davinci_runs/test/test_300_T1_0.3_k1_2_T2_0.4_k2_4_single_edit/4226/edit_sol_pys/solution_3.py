

x, y = map(int, input().split())  # 入力

if y % 2 == 0 and x * 2 <= y and y <= x * 4:  # 条件分岐
    print("Yes")
else:
    print("No")
