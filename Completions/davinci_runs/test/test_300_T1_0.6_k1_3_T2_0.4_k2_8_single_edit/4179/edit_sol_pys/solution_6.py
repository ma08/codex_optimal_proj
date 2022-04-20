
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    # n, m = 3, 3
    # a = [1, 2, 3]
    # b = [3, 2, 1]

    c = [a[i] + b[i] for i in range(n)]
    d = [a[i] - b[i] for i in range(n)]

    print(max(sum(c), sum(d)))

if __name__ == '__main__':
    main()
