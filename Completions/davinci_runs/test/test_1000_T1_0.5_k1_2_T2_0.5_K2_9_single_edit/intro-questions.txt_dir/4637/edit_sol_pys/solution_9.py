
import sys

def solve_problem():
    # Get number of test cases
    t = int(sys.stdin.readline())

    # Iterate over test cases
    for i in range(t):
        # Read input
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))

        # Sort both arrays
        a.sort()
        b.sort(reverse=True)

        # Compute sum of first k elements of a
        # and replace the first k elements of a
        # with the first k elements of b
        result = sum(a[0:k])
        a[0:k] = b[0:k]

        # Print result
        sys.stdout.write(str(result)+'\n')


if __name__ == '__main__':
    solve_problem()
