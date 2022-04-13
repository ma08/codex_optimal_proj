
def main():
    x1, y1, x2, y2, t = map(int, input().split())

    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == t ** 2:
        print("Y")

    else:
        print("N")

main()
