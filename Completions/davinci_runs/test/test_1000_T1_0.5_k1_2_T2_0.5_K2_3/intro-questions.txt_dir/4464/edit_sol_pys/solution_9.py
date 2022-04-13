

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    if c % a == 0 or c % b == 0 or a % b == 0 or b % a == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
