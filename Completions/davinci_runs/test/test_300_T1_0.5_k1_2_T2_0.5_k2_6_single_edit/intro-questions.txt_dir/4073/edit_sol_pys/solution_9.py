

def main():
    """
    This is the main function.
    """

    # Read the input data
    n, p = map(int, input().split())
    a = list(map(int, input().split()))[:n]

    # Solve the problem
    solution = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    if a[i] + a[j] > a[k] and a[j] + a[k] > a[i] and a[k] + a[i] > a[j]:
                        solution += 1

    # Print the solution
    print(solution)

if __name__ == "__main__":
    main()
