

import math

def main():
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        x = int(math.sqrt(n))
        if x * x == n:
            print(2 * x - 2)
        else:
            if x * (x + 1) >= n:
                print(2 * x - 1)
            else:
                print(2 * x)

if __name__ == '__main__':
    main()