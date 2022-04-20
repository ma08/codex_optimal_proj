

import sys

def main():
    A, B = map(int, input().split())

    if A == 1:
        print(B)
    elif A == 2:
        print(B * 2)
    elif A == 3:
        print(B * 3)
    else:
        print(B)


if __name__ == '__main__':
    main()
