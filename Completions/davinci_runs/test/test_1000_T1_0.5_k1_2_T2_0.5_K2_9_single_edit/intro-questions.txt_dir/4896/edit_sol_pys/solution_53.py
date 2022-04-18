
import sys

def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]
    assert len(bricks) == n

    # Count towers
    towers = 0
    for i in range(n):
        if i == 0 or bricks[i] > bricks[i-1]:
            towers += 1
    print(towers)

if __name__ == "__main__":
    main()
