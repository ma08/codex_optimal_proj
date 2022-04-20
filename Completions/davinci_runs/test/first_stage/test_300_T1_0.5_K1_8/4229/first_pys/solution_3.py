

import math

def main():
    n = int(input())
    n1 = (n - 1) // 3
    n2 = (n - 1) // 5
    n3 = (n - 1) // 15
    print(int((3 * n1 * (n1 + 1) + 5 * n2 * (n2 + 1) - 15 * n3 * (n3 + 1)) / 2))

if __name__ == '__main__':
    main()