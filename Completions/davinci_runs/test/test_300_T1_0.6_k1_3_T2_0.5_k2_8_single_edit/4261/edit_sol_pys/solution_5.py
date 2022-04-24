

a, b, c = map(int, input().split())  # 入力された数値をa,b,cに代入

while 1:
    if b + c <= a:  # b+cがa以下ならば
        print(0)  # 0を出力
        break
    elif b + c > a:
        print(b + c - a)
        break
