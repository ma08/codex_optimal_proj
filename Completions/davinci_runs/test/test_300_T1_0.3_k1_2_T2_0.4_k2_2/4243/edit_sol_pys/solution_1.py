

import sys

def main():
    n = int(input())
    print(n // 500 * 1000 + n % 500 // 5 * 5)

if __name__ == "__main__":
    main()
