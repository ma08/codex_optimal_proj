

def main():
    """
    This is the main function.
    """

    # Read the input data
    n = int(input())
    a = list(map(int, input().split()))

    # Solve the problem
    solution = 1

    for i in range(1, n):
        if a[i] > a[i-1]:
            solution += 1

    # Print the solution
    print(solution)

if __name__ == "__main__":
    main()
