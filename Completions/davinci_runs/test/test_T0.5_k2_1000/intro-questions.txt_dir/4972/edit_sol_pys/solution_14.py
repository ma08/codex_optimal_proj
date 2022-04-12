
import sys
import math

def main():
    x = int(sys.stdin.readline())

    k = 0
    while x > 0:
        k += 1
        x //= 2

    print(k)

if __name__ == "__main__":
    main()
