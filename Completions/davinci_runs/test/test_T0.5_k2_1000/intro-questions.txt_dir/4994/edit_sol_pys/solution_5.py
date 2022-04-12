

def main():
    x1, y1 = map(int, input().split())  # 入力を受け取る
    x2, y2 = map(int, input().split())  # 入力を受け取る
    x3, y3 = map(int, input().split())  # 入力を受け取る
    x4 = 0
    y4 = 0
    if x1 == x2:  # x1とx2が同じなら
        x4 = x3
    elif x2 == x3:  # x2とx3が同じなら
        x4 = x1
    else:  # それ以外なら
        x4 = x2
    if y1 == y2:  # y1とy2が同じなら
        y4 = y3
    elif y2 == y3:
        y4 = y1
    else:
        y4 = y2
    print(x4, y4)


main()
