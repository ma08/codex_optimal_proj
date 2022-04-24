

import math
import sys

# The main function.
def main():
    # Read the number of weights from the standard input.
    n = int(input()) # 5

    # Read the weights from the standard input.
    w = list(map(int, input().split())) # 2 3 3 4 5

    # Calculate the minimum possible absolute difference of S1 and S2.
    s_1 = []
    s_2 = []
    for i in range(n):
        s_1.append(sum(w[:i+1])) # [2, 5, 8, 12, 17]
        s_2.append(sum(w[i+1:])) # [15, 12, 9, 5]
    ans = math.inf
    for i in range(n):
        ans = min(ans, abs(s_1[i] - s_2[i]))

    # Print the answer.
    print(ans)

# Execute the program.
if __name__ == '__main__':
    main()
