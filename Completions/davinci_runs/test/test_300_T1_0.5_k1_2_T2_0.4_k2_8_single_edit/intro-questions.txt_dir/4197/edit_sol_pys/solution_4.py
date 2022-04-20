import sys


def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(enumerate(a, 1))
    b = sorted(b, key=lambda x: x[1])
    b = [i[0] for i in b]
    for i in b:
        print(i)


if __name__ == '__main__':
    main()
