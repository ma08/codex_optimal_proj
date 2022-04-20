

def main():
    x1, y1, x2, y2 = map(int, input().split())  # first rectangle
    x3, y3, x4, y4 = map(int, input().split())  # second rectangle
    x5, y5, x6, y6 = map(int, input().split())  # third rectangle

    if x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3:  # first and second
        if x1 >= x6 or x2 <= x5 or y1 >= y6 or y2 <= y5:  # first and third
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    main()
