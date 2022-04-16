

def main():
    # Get input
    w, a, b = map(int, input().split())
    # If a and b are equal, no movement is needed
    if a == b:
        print(0)
    # If the distance between a and b is less than the width of the rectangle, then movement is needed
    elif abs(a-b) < w:
        print(0)
    # Otherwise, the distance between the two rectangles should be printed
    else:
        print(abs(a-b)-w)

if __name__ == '__main__':
    main()
