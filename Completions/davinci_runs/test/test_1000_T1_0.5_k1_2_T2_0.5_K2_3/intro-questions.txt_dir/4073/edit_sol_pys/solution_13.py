
def main():
    """
    This is the main function.
    """

    # Read the input data
    num_integers = int(input())
    integers = list(map(int, input().split()))

    # Solve the problem
    num_triangles = 0

    for i in range(num_integers):
        for j in range(i+1, num_integers):
            for k in range(j+1, num_integers):
                if integers[i] != integers[j] and integers[j] != integers[k] and integers[k] != integers[i]:
                    if integers[i] + integers[j] > integers[k] and integers[j] + integers[k] > integers[i] and integers[k] + integers[i] > integers[j]:
                        num_triangles += 1

    # Print the solution
    print(num_triangles)

if __name__ == "__main__":
    main()
