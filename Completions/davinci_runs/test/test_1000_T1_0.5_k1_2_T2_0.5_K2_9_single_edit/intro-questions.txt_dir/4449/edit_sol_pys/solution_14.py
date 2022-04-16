

from math import sqrt

def main():
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        print(solve(n, a))

def solve(n, a):
    a.sort()
    for i in range(0, n, 4):
        if a[i] != a[i+1] or a[i+2] != a[i+3]:
            return "NO"
        if a[i] != a[i+2]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    main()
