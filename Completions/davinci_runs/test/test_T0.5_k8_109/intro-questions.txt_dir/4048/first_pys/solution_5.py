

# Accepted.

import math

def main():
    N = int(input())
    x, y = 1, 1
    count = 0

    while True:
        count += 1
        if N == x * y:
            break
        elif N > x * y:
            if x < y:
                x += 1
            else:
                y += 1
        elif N < x * y:
            if x < y:
                y -= 1
            else:
                x -= 1

    print(count)

if __name__ == '__main__':
    main()