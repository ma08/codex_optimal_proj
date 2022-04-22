

def main():
    """
    This is the main function.
    """

    # Read the input data
    _n = int(input())
    _a = list(map(int, input().split()))

    # Solve the problem
    solution = 0

    for _i in range(_n):
        for _j in range(_i+1, _n):
            for _k in range(_j+1, _n):
                if _a[_i] != _a[_j] and _a[_j] != _a[_k] and _a[_k] != _a[_i]:
                    if _a[_i] + _a[_j] > _a[_k] and _a[_j] + _a[_k] > _a[_i] and _a[_k] + _a[_i] > _a[_j]:
                        solution = solution + 1

    # Print the solution
    print(solution)

if __name__ == "__main__":
    main()
