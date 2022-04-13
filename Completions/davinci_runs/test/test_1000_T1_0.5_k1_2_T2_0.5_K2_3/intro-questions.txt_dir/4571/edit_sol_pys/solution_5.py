

from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    if m == 0:
        print(n * 100)
    elif m == 1:
        print(n * 100 + 1900)
    else:
        print(n * 100 + 1900 * sum([(0.5) ** i for i in range(1, m)]))

if __name__ == '__main__':
    main()
