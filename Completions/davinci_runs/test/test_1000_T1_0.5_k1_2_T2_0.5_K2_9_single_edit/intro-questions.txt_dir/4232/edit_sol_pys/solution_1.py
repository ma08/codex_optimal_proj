

import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        a, b, c = [int(x) for x in sys.stdin.readline().strip().split()]
        if a + b > c:
            print("Case #" + str(i + 1) + ": true")
        else:
            print("Case #" + str(i + 1) + ": false")

if __name__ == "__main__":
    main()
