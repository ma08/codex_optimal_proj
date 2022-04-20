

import sys
import math

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i] + b[i] for i in range(n)]
    c = sorted(c)
    cnt = sum(1 for i in range(n) if c[i] == 0)
    print(cnt)

if __name__ == "__main__":
    main()
