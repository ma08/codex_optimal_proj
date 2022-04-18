

import sys

def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    d = [int(x) for x in input().split()]
    for i in range(m):
        print(a[i] + b[i] + c[i] + d[i])

if __name__ == "__main__":
    main()
