

def main():
    #Get input
    x1, y1 = map(int, input().split()) # Point 1
    x2, y2 = map(int, input().split()) # Point 2
    x3, y3 = map(int, input().split()) # Point 3

    #Calculate final X and Y values
    x4 = 0 # X value for Point 4
    y4 = 0 # Y value for Point 4

    # Calculate X value for Point 4
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1

    # Calculate Y value for Point 4
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1

    #Print final X and Y values
    print(x4, y4)

if __name__ == "__main__":
    main()
