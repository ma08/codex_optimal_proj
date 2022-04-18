
import sys


def solver(n, a, b):
    if a[0] != b[0]:
        return "NO"

    for i in range(1, n - 1):
        if a[i] > b[i]:
            return "NO"
        if a[i] < b[i] and a[i + 1] < b[i + 1]:
            return "NO"

    if a[-1] > b[-1]:
        return "NO"

    return "YES"


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    print(solver(n, a, b))
