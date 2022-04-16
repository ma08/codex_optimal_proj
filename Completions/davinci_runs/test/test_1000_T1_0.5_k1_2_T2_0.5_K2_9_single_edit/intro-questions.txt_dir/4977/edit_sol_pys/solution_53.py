

def main():
    """
    Solve the problem!
    """
    start = [int(i) for i in input().split()] # read in starting location
    end = [int(i) for i in input().split()] # read in ending location
    charge = int(input()) # read in charge

    if abs(end[0] - start[0]) + abs(end[1] - start[1]) <= charge: # if distance is less than or equal to charge
        print("Y")
    else: # otherwise
        print("N")

if __name__ == "__main__":
    main()
