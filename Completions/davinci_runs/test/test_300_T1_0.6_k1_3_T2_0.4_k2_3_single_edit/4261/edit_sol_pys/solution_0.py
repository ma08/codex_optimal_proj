
a, b, c = map(int, input().split())  # a = 材料, b = 値段, c = 値段

while 1:
    if b + c <= a:  # 値段が材料よりも小さい場合
        print(0)
        break
    elif b + c > a:  # 値段が材料よりも大きい場合
        print(b + c - a)
        break
