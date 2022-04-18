
import sys
import sys

def main():
    # Read input
    n = int(input())
    bricks = [int(x) for x in input().split()]
    assert(len(bricks) == n)

    # Count towers
    towers = 0
    for i in range(n):
        if (i == 0) or (bricks[i] > bricks[i-1]):
            towers += 1

    # Print result
    print(towers,end="")

if __name__ == '__main__':
    main()
