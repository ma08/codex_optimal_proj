

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = [int(x) for x in sys.stdin.readline().strip().split()]
    a.sort()
    c = 0
    for i in range(n):
        c += 1
        if a[i] >= c:
            c = a[i] + 1
    print(c)

if __name__ == "__main__":
    main()
