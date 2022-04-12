

def main():
    # Get inputs
    x1, y1 = map(int, input().split())  # first point
    x2, y2 = map(int, input().split())  # second point
    x3, y3 = map(int, input().split())  # third point

    # Calculate the final X and Y values
    x4 = 0  # final X value
    y4 = 0  # final Y value

    # Calculate the final X value
    if x1 == x2:
        x4 = x3
        x4 = x1

    # Calculate the final Y value
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1

    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:  # y1 == y2
        y4 = y3

    # Print the final X and Y values
    print(x4, y4)

if __name__ == "__main__":
    main()
