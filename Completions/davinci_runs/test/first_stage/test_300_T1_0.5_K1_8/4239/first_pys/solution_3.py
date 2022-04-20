

import math

def main():
    n = int(input())
    x = 0
    while n > 0:
        x = x + 1
        if n % 6 == 0:
            n = n // 6
        else:
            n = n // 9
    print(x)

if __name__ == '__main__':
    main()