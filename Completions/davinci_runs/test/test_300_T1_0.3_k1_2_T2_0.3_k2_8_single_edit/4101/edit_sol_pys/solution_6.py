

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = [int(sys.stdin.readline()) for _ in range(n)]
    if a == sorted(a):
        print("YES")
        print("0 " * n)
        print("0 " * m)
    else:
        print("NO")

if __name__ == "__main__":
    main()
