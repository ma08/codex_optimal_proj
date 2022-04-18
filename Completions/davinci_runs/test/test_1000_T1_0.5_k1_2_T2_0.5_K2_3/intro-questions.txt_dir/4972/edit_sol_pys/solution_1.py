
import sys
import math

def main():
    n = int(sys.stdin.readline())

    x = n
    k = 0
    while x > 1:
        k += 1
        x //= 2

    print(k)

if __name__ == "__main__":
    main()
