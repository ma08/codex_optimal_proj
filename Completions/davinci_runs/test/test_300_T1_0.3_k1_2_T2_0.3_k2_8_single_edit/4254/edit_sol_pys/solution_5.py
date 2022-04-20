

s, w = map(int, input().split())  # 入力を数値に変換

if s <= w:  # 条件分岐
    print('unsafe')
else:
    print('safe')
