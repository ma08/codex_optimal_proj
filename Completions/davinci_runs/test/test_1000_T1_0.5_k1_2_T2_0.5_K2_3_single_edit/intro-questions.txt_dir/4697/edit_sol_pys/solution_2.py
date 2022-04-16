

import sys

def main():
    """
    n: the number of S-shaped pieces
    m: the number of c-shaped pieces
    """
    n, m = map(int, input().split())
    print(min(m // 2, n))

if __name__ == '__main__':
    main()
