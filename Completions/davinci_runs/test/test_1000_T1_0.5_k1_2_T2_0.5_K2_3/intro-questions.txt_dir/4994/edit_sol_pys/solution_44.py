

def main():
    """
    Read three points and print the fourth point.
    """
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    x4, y4 = x3, y2 if x4 == x1 and y4 == y1 else:
        x4, y4 = x2, y3
    elif x4 == x2 and y4 == y2:
        x4, y4 = x1, y3
    print(x4, y4)

if __name__ == "__main__":
    main()
