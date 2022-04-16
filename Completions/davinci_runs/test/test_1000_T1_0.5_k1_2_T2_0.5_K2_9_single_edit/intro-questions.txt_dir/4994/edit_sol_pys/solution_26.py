

def main():
    """
    Reads three points and prints the fourth point.
    """
    x1, y1 = map(int, input().split())  # Read in x1, y1
    x2, y2 = map(int, input().split())  # Read in x2, y2
    x3, y3 = map(int, input().split())  # Read in x3, y3

    x4, y4 = x3, y2  # Set x4, y4 to x3, y2
    if x4 == x1 and y4 == y1:  # If x4, y4 are the same as x1, y1
        x4, y4 = x2, y3  # Set x4, y4 to x2, y3
    elif x4 == x2 and y4 == y2:  # If x4, y4 are the same as x2, y2
        x4, y4 = x1, y3  # Set x4, y4 to x1, y3
    print(x4, y4)  # Print x4, y4

if __name__ == "__main__":
    main()
