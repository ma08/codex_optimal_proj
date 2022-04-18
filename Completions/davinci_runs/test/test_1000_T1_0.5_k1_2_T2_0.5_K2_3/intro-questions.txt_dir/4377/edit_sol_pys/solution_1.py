

from sys import stdin


def main():
    line = stdin.readline().strip()
    if line.startswith('1'):
        print(len(line) - 1)
    else:
        print(len(line))


if __name__ == '__main__':
    main()
