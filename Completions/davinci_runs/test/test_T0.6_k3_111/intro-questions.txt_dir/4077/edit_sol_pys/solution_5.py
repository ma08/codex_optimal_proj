
import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    idx = [0] * (2 * 10 ** 5 + 2)
    s = 0
    for i in range(1, n + 1):
        s += idx[a[i - 1] + 1]
        idx[a[i - 1] + 1] += 1

    print(s)

if __name__ == "__main__":
    main()
