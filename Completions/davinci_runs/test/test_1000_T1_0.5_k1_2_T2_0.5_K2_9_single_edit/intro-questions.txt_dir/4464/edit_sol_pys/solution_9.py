

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    if c % a == b:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
