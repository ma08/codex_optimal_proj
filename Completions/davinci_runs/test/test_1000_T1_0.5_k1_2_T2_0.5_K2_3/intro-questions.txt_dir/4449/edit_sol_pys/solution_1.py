

from math import sqrt

def main():
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        print(solve(n, a))

def solve(n, a):
    a.sort()
    if len(a) % 2 != 0:
        return "NO"
    for i in range(0, len(a), 2):
        if a[i] != a[i + 1]:
            return "YES"
    return "YES"

if __name__ == "__main__":
    main()
