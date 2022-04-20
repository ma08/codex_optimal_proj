

import sys
import math

def main():
    # Read Input
    x = int(sys.stdin.readline())

    # Calc
    ans = math.ceil(math.log(x/100, 1.01))

    # Print Answer
    print(ans)

if __name__ == '__main__':
    main()
