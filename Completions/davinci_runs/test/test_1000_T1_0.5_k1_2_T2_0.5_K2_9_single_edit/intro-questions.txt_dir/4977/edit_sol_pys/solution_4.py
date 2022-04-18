

def main():
    """
    Solve the problem!
    """
    start = [int(i) for i in input().split()] # list comprehension, turns input into a list of ints
    end = [int(i) for i in input().split()] # list comprehension, turns input into a list of ints
    charge = int(input()) # turns input into an int

    if abs(end[0] - start[0]) + abs(end[1] - start[1]) <= charge:
        print("Y")
    else:
        print("N")

if __name__ == "__main__":
    main()
