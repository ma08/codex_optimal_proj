

def main():
    """
    Solve the problem!
    """
    start = [int(i) for i in input().split()]  # start is a list of integers
    end = [int(i) for i in input().split()]  # end is a list of integers
    charge = int(input())

    if abs(end[0] - start[0]) + abs(end[1] - start[1]) <= charge:
        print("Y")
    else:
        print("N")

if __name__ == "__main__":
    main()
