
import sys
import math

def main():
    x = int(sys.stdin.readline()) # read the first line

    k = 0 # initialize k
    while x > 1:
        k += 1
        x //= 2

    print(k)

if __name__ == "__main__":
    main()
