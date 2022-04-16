

import sys

def main():
    a, b, c, d = [int(i) for i in sys.stdin.readline().split()]
    if (abs(a - c) <= d) or (abs(b - c) <= d):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
