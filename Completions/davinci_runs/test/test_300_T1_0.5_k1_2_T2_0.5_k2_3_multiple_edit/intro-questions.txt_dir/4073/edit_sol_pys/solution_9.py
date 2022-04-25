

def main():
    """
    This is the main function.
    """

    # Read the input data
    n = int(input())  # number of sticks
    a = list(map(int, input().split()))  # length of each stick

    # Solve the problem
    solution = 0  # number of possible triangles

    for i in range(n):
        for j in range(i+1, n):  # loop over all pairs of sticks
            for k in range(j+1, n):  # loop over all triplets of sticks
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:  # check if they are all different
                    if a[i] + a[j] > a[k] and a[j] + a[k] > a[i] and a[k] + a[i] > a[j]:  # check if they form a triangle
                        solution += 1

    # Print the output
    print(solution)

if __name__ == "__main__":
    main()
