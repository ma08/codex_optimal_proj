import sys


def main():
    n = int(sys.stdin.readline())
    values = sorted(map(int, sys.stdin.readline().split()))
    last = values.pop(0)
    while len(values) > 1:
        last = max(int(last / values.pop(0)), 1)
    print(last * values.pop(0))


if __name__ == "__main__":
    main()
