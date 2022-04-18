
# https://atcoder.jp/contests/abc081/tasks/abc081_a
import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    print((n - 1) * (n - 2) // 2 + m)

if __name__ == "__main__":
    main()
