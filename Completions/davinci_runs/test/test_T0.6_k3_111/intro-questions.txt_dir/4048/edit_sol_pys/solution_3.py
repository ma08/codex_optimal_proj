import sys
import math

def main():
    n = int(sys.stdin.readline())

    if n == 1:
        print(0)
    else:
        move = 0
        i = 1
        j = 1

        while i < n or j < n:
            if i == j:
                i += 1
            elif i < j:
                i += 1
            elif i > j:
                j += 1

            move += 1

        print(move)

if __name__ == "__main__":
    main()
