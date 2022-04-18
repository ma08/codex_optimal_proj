
def main():
    """
    Read three points and print the fourth point.
    """
    x1, y1 = map(int, input().split())  # For example, this is OK.
    x2, y2 = map(int, input().split())  # For example, this is OK.
    x3, y3 = map(int, input().split())  # For example, this is OK.

    x4 = x3
    y4 = y2
    if x4 == x1 and y4 == y1:  # For example, this is OK.
        x4 = x2
        y4 = y3
    elif x4 == x2 and y4 == y2:  # For example, this is OK.
        x4 = x1
        y4 = y3
    print(x4, y4)  # For example, this is OK.


if __name__ == "__main__":  # For example, this is OK.
    main()
