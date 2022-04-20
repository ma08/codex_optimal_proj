

def main():
    """
    This is the main function.
    """

    # Read the input data
    n = int(input())
    a = list(map(int, input().split()))

    # Solve the problem
    solution = 0

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            for k in range(j+1, len(a)):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:  # check if the sides are not equal
                    if a[i] + a[j] > a[k] and a[j] + a[k] > a[i] and a[k] + a[i] > a[j]:  # check if the sides can form a valid triangle
                        solution += 1

    # Print the solution
    print(solution)

if __name__ == "__main__":
    main()
