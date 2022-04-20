
from math import gcd

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    c.sort()
    cnt = 0
    for i in range(n):
        cnt += len(c) - (bisect_right(c, b[i]) - 1)
    print(cnt)

if __name__ == "__main__":
    main()
