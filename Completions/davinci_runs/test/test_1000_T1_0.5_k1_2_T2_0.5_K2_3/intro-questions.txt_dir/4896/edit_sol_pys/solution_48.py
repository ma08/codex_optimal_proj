
import sys

def main():
    # read input
    n = int(sys.stdin.readline())
    bricks = [int(x) for x in sys.stdin.readline().split()]
    assert(len(bricks) == n)

    # count towers
    towers = 0
    for i in range(n):
        if (i == 0) or (bricks[i] > bricks[i-1]):
            towers += 1

    # print result
    print(towers)

if __name__ == '__main__':
    main()
