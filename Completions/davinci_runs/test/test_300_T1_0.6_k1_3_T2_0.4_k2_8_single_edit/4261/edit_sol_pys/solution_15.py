import sys


def main():
    for line in sys.stdin:
        a, b, c = map(int, line.split())
        print("{}".format(c - min(a-b, c)))

if __name__ == "__main__":
    main()
