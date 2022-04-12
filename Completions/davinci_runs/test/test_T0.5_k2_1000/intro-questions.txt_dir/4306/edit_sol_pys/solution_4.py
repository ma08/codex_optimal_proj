
a, b, c, d = map(int, input().split()) # a,b,c,dに値を入力
if c < a: # cがaより小さい場合
    if d <= a: # dがa以下の場合
        print(0)
    elif d <= b: # dがb以下の場合
        print(d - a)
    else: # dがbより大きい場合
        print(b - a)
elif c < b: # cがaより大きくbより小さい場合
    if d <= b: # dがb以下の場合
        print(d - c)
    else: # dがbより大きい場合
        print(b - c)
else: # cがbより大きい場合
    print(0)
