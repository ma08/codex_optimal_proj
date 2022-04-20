

def main():
    x1, y1, x2, y2 = map(int, input().split())  # 左下と右上の座標
    x3, y3, x4, y4 = map(int, input().split())  # 左下と右上の座標
    x5, y5, x6, y6 = map(int, input().split())  # 左下と右上の座標

    if x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3:  # 左下が右上より右か上にあるか
        if x1 >= x6 or x2 <= x5 or y1 >= y6 or y2 <= y5:  # 左下が右上より右か上にあるか
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    main()
