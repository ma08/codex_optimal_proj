import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    mx, mn = max(a), min(a)
    if mx == mn or mx - mn == 1 or (a.count(mx) == 1 and a.count(mn) == 1):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
