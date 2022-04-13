

def main():
    # Get inputs
    x1, y1 = map(int, input().split()) # x1, y1 = int(input()), int(input())
    x2, y2 = map(int, input().split()) # x2, y2 = int(input()), int(input())
    x3, y3 = map(int, input().split()) # x3, y3 = int(input()), int(input())

    # Calculate the final X and Y values
    x4 = 0
    y4 = 0
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1

    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1

    # Print the final X and Y values
    print(x4, y4)

if __name__ == "__main__":
    main()
