

import sys
import math

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    c = [a[i] + b[i] for i in range(n)]
    print(c.count(0))

if __name__ == "__main__":
    main()
