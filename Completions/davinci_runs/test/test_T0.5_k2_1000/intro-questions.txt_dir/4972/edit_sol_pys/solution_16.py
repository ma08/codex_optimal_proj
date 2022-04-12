
import sys
import math

def main():
    x = int(sys.stdin.readline())
    k = int(math.log(x, 2)) + 1
    print(2 ** k)

if __name__ == "__main__":
    main()
