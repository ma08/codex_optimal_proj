

def main():
    """
    This is the main function.
    """

    # Read the input data.
    n = int(input())        # number of cards
    a = list(map(int, input().split()))   # length of the cards

    # Solve the problem.
    solution = 0    # number of possible triangles

    for i in range(n):
        for j in range(i+1, n):   # loop through all the cards
            for k in range(j+1, n):   # loop through all the cards
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    if a[i] + a[j] > a[k] and a[j] + a[k] > a[i] and a[k] + a[i] > a[j]:   # check if it is a triangle
                        solution += 1

    # Print the solution.
    print(solution)   # print the number of triangles

if __name__ == "__main__":
    main()
