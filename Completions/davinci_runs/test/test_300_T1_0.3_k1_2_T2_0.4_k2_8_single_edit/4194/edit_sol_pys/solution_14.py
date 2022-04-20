

from sys import stdin

def main():
    n = int(stdin.readline())
    numbers = [int(x) for x in stdin.readline().split()]

    for x in numbers:
        if x % 2 == 0:
            print(x, end=' ')


if __name__ == '__main__':
    main()
