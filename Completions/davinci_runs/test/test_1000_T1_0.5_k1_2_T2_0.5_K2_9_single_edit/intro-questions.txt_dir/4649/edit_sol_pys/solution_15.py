


def helper(s, n):
    if n % 3 == 0:
        return 0
    else:
        if k == 1:
            return 1
        elif k == 2:
            if n % 3 == 1:
                return 2
            else:
                return 1
        else:
            if n % 3 == 2:
                return 1
            else:
                return 2
import sys

if __name__ == "__main__":
    q = int(sys.stdin.readline())

    for _ in range(q):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()

        print(helper(s, n))
