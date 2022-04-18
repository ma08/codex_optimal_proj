import sys


def main():
    args = sys.stdin.readlines()
    n = int(args[0])
    for i in range(1, n+1):
        a, b, c = [int(x) for x in args[i].split()]


def solve(a, b, c):
    for i in range(a, b+1):
        if i % c == 0:
            return i
    return -1
        print("Case #{}: {}".format(i, solve(a, b, c)))

if __name__ == '__main__':
    main()
