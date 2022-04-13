

def main():
    """
    Solve the problem
    """
    start = [int(i) for i in raw_input().split()]
    end = [int(i) for i in raw_input().split()]
    charge = int(raw_input())

    if abs(end[0] - start[0]) + abs(end[1] - start[1]) <= charge:
        print("Y")
    else:
        print("N")

if __name__ == "__main__":
    main()
