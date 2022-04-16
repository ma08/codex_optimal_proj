

import sys

    print("Hello")
def main():
    a, b, c, d = [int(i) for i in sys.stdin.readline().split()]
    if (abs(a - b) <= d) and (abs(b - c) <= d):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
