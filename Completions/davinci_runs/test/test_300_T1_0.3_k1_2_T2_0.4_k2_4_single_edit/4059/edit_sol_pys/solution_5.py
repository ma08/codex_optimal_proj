

import math
import sys


def main():
    N = int(input())
    count = 0
    for a in range(1, int(math.sqrt(N)) + 1):
        for b in range(1, int(math.sqrt(N)) + 1):
            if a * b + b > N:
                break
            if (N - b) % a == 0:
                count += 1
    print(count)



if __name__ == '__main__':
    main()
