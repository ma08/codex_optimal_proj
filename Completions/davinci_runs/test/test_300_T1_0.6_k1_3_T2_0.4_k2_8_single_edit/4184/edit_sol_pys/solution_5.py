

import math
import sys

# The main function.
def main():
    # Read the number of weights from the standard input.
    n = int(input())

    # Read the weights from the standard input.
    w = list(map(int, input().split()))

    # Calculate the minimum possible absolute difference of S1 and S2.
    s1 = []
    s2 = []
    for i in range(n):
        s1.append(sum(w[:i+1]))
        s2.append(sum(w[i+1:]))
    ans = math.inf
    for i in range(n):
        ans = min(ans, abs(s1[i] - s2[i]))

    # Print the answer.
    print(ans)

# Execute the program.
if __name__ == '__main__':
    main()
