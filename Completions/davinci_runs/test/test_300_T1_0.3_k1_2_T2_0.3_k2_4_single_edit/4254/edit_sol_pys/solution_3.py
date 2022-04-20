

s, w = map(int, input().split())  # 入力を2つに分ける

if s <= w:  # 条件分岐
    print('unsafe')
else:
    print('safe')
