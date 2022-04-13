


def solve_problem():
    # Get number of test cases and number of elements
    t, n = map(int, input().split())

    # Iterate over test cases
    for i in range(t):
        # Read input
        # Read input
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        # Sort both arrays
        a.sort()
        b.sort(reverse=True)

        # Compute sum of first k elements of a and replace
        # the first k elements of a with the first k elements of b
        result = sum(a[0:k])
        a[0:k] = b[0:k]

        # Print result
        print(result)


if __name__ == '__main__':
    solve_problem()
