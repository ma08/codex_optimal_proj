

import sys

# The main function.
def main():
    # Read the number of elements from the standard input.
    n = int(sys.stdin.readline())

    # Read the elements from the standard input.
    a = list(map(int, sys.stdin.readline().split()))

    # Calculate the number of inversions.
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                ans += 1

    # Print the answer.
    sys.stdout.write(str(ans) + '\n')

# Execute the program.
if __name__ == '__main__':
    main()
