

def main():
    """
    Reads three points and prints the fourth point
    """
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    x4, y4 = x3, y3
    if x4 == x1 and y4 == y1 or x4 == x2 and y4 == y2:
        x4, y4 = x2, y2
    elif x4 == x1 and y4 == y1 or x4 == x3 and y4 == y3:
        x4, y4 = x3, y3
    print(x4, y4, end=" ")

if __name__ == "__main__":
    main()
