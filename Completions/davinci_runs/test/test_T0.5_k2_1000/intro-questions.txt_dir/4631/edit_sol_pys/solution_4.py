
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))  # x = [1, 2, 3]
    x.sort()  # x = [1, 2, 3]
    y = [0] * m  # y = [0, 0, 0, 0, 0]
    for i in range(m):
        y[i] = x[i % n]
        x[i % n] += 1
    print(sum(y))
    print(' '.join(map(str, y)))


if __name__ == "__main__":
    main()
