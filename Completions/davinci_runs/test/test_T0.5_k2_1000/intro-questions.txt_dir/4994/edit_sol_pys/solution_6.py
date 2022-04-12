

def main():
    """
    Reads three points and prints the fourth point
    """
    x1, y1 = map(int, input().split()) # read first point
    x2, y2 = map(int, input().split()) # read second point
    x3, y3 = map(int, input().split()) # read third point

    x4, y4 = x3, y2 # set fourth point
    if x4 == x1 and y4 == y1: # check if x4, y4 is the first point
        x4, y4 = x2, y3 # set fourth point to second point
    elif x4 == x2 and y4 == y2: # check if x4, y4 is the second point
        x4, y4 = x1, y3 # set fourth point to first point
    print(x4, y4) # print fourth point

if __name__ == "__main__":
    main()
