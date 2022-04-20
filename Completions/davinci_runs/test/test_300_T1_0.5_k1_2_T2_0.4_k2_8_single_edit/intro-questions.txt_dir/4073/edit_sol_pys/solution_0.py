

def main():
    """
    This is the main function.
    """

    # Read the input data
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))  # n
    b = list(map(int, input().split()))  # m

    # Solve the problem
    solution = []

    for i in range(m):
        for j in range(n):
            if a[j] % b[i] == 0:
                solution.append(a[j])
                break

    # Print the solution
    print(len(solution))

if __name__ == "__main__":
    main()
