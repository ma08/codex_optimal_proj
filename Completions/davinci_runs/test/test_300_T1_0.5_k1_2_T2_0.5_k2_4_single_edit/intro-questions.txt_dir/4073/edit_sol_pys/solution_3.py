

def main():
    """
    This is the main function.
    """

    # Read the input data
    n = int(input())
    a = list(map(int, input().split()))

    # Solve the problem
    solution = 0

    for x in range(n):
        for y in range(x+1, n):
            for z in range(y+1, n):
                if a[x] != a[y] and a[y] != a[z] and a[z] != a[x]:
                    if a[x] + a[y] > a[z] and a[y] + a[z] > a[x] and a[z] + a[x] > a[y]:
                        solution = solution + 1

    # Print the solution
    print(solution)

if __name__ == "__main__":
    main()
