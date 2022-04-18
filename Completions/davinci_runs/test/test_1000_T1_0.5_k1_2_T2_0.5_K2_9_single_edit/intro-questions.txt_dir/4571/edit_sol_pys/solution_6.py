

from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    if m == 0: # first line
        print(n * 100)
    elif m == 1: # second line
        print(n * 100 + 1900)
    else: # third line
        print(n * 100 + 1900 * sum([(1 / 2) ** i for i in range(1, m + 1)]))

if __name__ == '__main__':
    main()
