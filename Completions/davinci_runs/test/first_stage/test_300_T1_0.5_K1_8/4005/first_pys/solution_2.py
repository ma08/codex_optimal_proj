

def main():
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    x3, y3, x4, y4 = [int(x) for x in input().split()]
    x5, y5, x6, y6 = [int(x) for x in input().split()]

    if x1 < x3 and x2 > x4 and y1 < y3 and y2 > y4 and x1 < x5 and x2 > x6 and y1 < y5 and y2 > y6:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()