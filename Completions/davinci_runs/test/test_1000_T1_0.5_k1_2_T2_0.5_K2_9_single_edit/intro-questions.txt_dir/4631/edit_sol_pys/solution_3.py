
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))  # 1 2 3 4
    x.sort()  # 1 2 3 4
    y = [0] * m  # 0 0 0 0
    for i in range(m):  # 0 1 2 3
        y[i] = x[i % n]  # 1 2 3 4
        x[i % n] += 1  # 2 3 4 5
    print(sum(y))  # 10
    print(' '.join(map(str, y)))  # 1 2 3 4 1 2 3 4


if __name__ == "__main__":
    main()
