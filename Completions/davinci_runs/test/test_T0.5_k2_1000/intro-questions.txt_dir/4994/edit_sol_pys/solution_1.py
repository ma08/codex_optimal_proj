

def main():
    x1, y1 = map(int, input().split()) # 1つ目の点の座標
    x2, y2 = map(int, input().split()) # 2つ目の点の座標
    x3, y3 = map(int, input().split()) # 3つ目の点の座標
    x4 = 0
    y4 = 0
    if x1 == x2: # 1つ目と2つ目の点がx座標が同じ場合
        x4 = x3
    elif x2 == x3: # 2つ目と3つ目の点がx座標が同じ場合
        x4 = x1
    else: # それ以外の場合
        x4 = x2
    if y1 == y2: # 1つ目と2つ目の点がy座標が同じ場合
        y4 = y3
    elif y2 == y3:
        y4 = y1
    else:
        y4 = y2
    print(x4, y4)


main()
