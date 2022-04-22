

import sys

    a = list(map(int, input().split()))
def main():
    n = int(input())
    m = int(input())
    b = list(map(int, input().split()))

    A = set(a)
    B = set(b)
    C = A.union(B)
    print(C)


if __name__ == "__main__":
    main()
