

def main():
    """
    Solve the problem!
    # Get starting and ending coordinates
    """
    start = [int(i) for i in input().split()]

    # Get charge
    end = [int(i) for i in input().split()]

    # Check if can get there
    charge = int(input())

    if abs(end[0] - start[0]) + abs(end[1] - start[1]) <= charge:
        print("Y")
    else:
        print("N")

if __name__ == "__main__":
    main()
