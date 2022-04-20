import sys

import math

def main():
    x = int(sys.stdin.readline())

    ans = math.log(x/100, 1.01)
    print(math.ceil(ans))

if __name__ == '__main__':
    main()
