import sys


def coconut(n):
    return n * (n + 1) // 2


def main():
    for line in sys.stdin:
        n = int(line)
        print(coconut(n))

if __name__ == "__main__":
    main()
