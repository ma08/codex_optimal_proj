
a, b, c, d = map(int, input().split())  # 複数数値入力
if d >= abs(a - c) or d >= abs(a - b) + abs(b - c):  # 条件分岐
    print('Yes')  # 出力
else:  # 条件分岐
    print('No')  # 出力
