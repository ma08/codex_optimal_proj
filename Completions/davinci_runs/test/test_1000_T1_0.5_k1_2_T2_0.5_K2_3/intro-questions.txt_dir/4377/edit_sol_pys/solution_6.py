
from sys import stdin


def main():
    s = stdin.readline().strip()
    if s.startswith('1'):
        print(len(s) - 1)
    else:
        print(len(s))


if __name__ == '__main__':
    main()
