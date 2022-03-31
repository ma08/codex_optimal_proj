

import sys

def main():
    n = int(sys.stdin.readline())
    # n = 5
    result = 0
    while n > 1:
        result += 1
        n >>= 1
    print(result)

if __name__ == "__main__":
    main()