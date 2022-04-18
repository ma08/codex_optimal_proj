

import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    a = [int(x) for x in sys.stdin.readline().strip().split()]
    m = int(sys.stdin.readline().strip())
    b = [int(x) for x in sys.stdin.readline().strip().split()]
    for i in range(m):
        if b[i] in a:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
