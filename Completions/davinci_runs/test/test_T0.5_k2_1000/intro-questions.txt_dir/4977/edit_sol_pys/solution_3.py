

def main():
    """
    Solve the problem!
    """
    start = [int(i) for i in input().split()]  # start point (x, y)
    end = [int(i) for i in input().split()]  # end point (x, y)
    charge = int(input())  # charge (integer)

    if abs(end[0] - start[0]) + abs(end[1] - start[1]) <= charge:  # if the distance is less than or equal to the charge
        print("Y")
    else:
        print("N")

if __name__ == "__main__":
    main()
