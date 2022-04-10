

import sys

def main():
    n, m, d = [int(x) for x in sys.stdin.readline().strip().split()]
    c = [int(x) for x in sys.stdin.readline().strip().split()]
    assert(len(c) == m)
    assert(sum(c) <= n)
    assert(1 <= n <= 1000)
    assert(1 <= m <= n)
    assert(1 <= d <= 1000)
    for i in range(m):
        assert(1 <= c[i] <= n)
    print("YES")
    print("0 " * n)

if __name__ == "__main__":
    main()