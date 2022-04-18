

def main():
    """
    Solve the problem!
    """
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    charge = int(input())

    if abs(end[0] - start[0]) + abs(end[1] - start[1]) <= charge:
        print("Y")
    else:
        print("N")

if __name__ == "__main__":
    main()
