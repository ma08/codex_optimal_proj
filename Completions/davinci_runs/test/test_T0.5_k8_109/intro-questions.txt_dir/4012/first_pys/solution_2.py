

import sys

def main():
    t = int(input())
    while t > 0:
        a, b, c = map(int, input().split())
        if b % a == 0 and c % b == 0:
            print(0)
            print(a, b, c)
        else:
            res = 0
            A = a
            B = b
            C = c
            if b % a != 0:
                if b % a == 1:
                    B = b + 1
                    res = res + 1
                else:
                    B = b - (b % a)
                    res = res + b % a
            if c % b != 0:
                if c % b == 1:
                    C = c + 1
                    res = res + 1
                else:
                    C = c - (c % b)
                    res = res + c % b
            print(res)
            print(A, B, C)
        t = t - 1

if __name__ == "__main__":
    main()