

import math

def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if a == b:
        print(1)
    else:
        print(a * b)

if __name__ == '__main__':
    main()