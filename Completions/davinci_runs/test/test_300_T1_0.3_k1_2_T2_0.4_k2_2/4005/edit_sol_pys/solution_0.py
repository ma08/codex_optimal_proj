

def main():
    x1, y1, x2, y2 = map(int, input().split())  # x1, y1, x2, y2: 長方形1の座標
    x3, y3, x4, y4 = map(int, input().split())  # x3, y3, x4, y4: 長方形2の座標
    x5, y5, x6, y6 = map(int, input().split())  # x5, y5, x6, y6: 長方形3の座標

    if x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3:  # 長方形1と長方形2が重なっていない
        if x1 >= x6 or x2 <= x5 or y1 >= y6 or y2 <= y5:  # 長方形1と長方形3が重なっていない
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    main()
