

from sys import stdin

def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    total = sum(a)
    nice = []
    for i, a_i in enumerate(a):
        if a_i == total - a_i:
            nice.append(i + 1)
    print(len(nice))
    print(*nice)


if __name__ == '__main__':
    main()