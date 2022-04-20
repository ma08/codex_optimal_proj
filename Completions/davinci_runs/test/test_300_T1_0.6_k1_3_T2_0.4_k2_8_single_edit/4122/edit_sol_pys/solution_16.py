import sys

def solve():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b // 2)
    else:
        print(0)

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    print(solve())
