

x, y = map(int, input().split())  # 複数数値入力

if y % 2 == 0 and x * 2 <= y and y <= x * 4:
    print("Yes")
else:
    print("No")
