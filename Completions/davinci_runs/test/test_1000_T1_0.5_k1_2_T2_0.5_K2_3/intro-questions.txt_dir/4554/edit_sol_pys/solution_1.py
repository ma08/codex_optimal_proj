

def main():
    # Get input
    width, a, b = map(int, input().split())
    # If a and b are equal, no movement is needed
    if a == b:
        print(0)
    # If the distance between a and b is less than the width of the rectangle, then movement is not needed
    elif abs(a-b) < width:
        print(0)
    # Otherwise, the distance between the two rectangles should be printed
    else:
        print(abs(a-b)-width)

if __name__ == '__main__':
    main()
