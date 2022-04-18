
import sys
import math

def main():
    n = int(sys.stdin.readline())

    for i in range(n):
        a = int(sys.stdin.readline())
        k = 0
        x = a
        while x > 1:
            k += 1
            x //= 2

    print(k)

if __name__ == "__main__":
    main()
