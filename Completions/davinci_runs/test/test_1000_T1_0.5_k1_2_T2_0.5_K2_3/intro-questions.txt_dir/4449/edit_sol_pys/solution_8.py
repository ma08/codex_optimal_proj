

from math import sqrt

def main():
    q = int(input())
    for a0 in range(int(q)):
        n = int(input())
        a = list(map(int, input().split(' ')))
        print(solve(n, a))

def solve(n, a):
    a.sort()
    for i in range(0, len(a), 4):
        if a[i] != a[i + 1] or a[i + 2] != a[i + 3]:
            return "NO"
        if a[i] != a[i + 2]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    main()
