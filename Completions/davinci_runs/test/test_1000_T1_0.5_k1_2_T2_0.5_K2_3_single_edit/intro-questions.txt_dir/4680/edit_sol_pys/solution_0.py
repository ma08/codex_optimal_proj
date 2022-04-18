
import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())


def solve():
    if a == b == c:
        print("YES")
    elif a == b or b == c or a == c:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    solve()
