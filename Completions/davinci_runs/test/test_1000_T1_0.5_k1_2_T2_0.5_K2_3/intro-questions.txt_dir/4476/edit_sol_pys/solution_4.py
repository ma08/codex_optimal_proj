
import sys
T = int(input())  # get the number of test cases

for _ in range(T):  # iterate over the test cases
    a, b = map(int, sys.stdin.readline().split())  # get the input
    ans = 0  # initialize answer
    # check if the difference is even or odd
    if a < b:
        if (b - a) % 2 == 0:
            ans = 1
        else:
            ans = 2
    elif a > b:
        if (a - b) % 2 == 0:
            ans = 2
        else:
            ans = 1
    else:
        ans = 0
    print(ans)
